import numpy as np
from typing import Dict, List, Optional, Tuple

from src.config import get_settings
from src.parser import Document, parse_all_documents
from src.embedder import Embedder
from src.bm25 import BM25Retriever
from src.storage import StorageManager


class HybridRetriever:
    """复合检索器：BM25 + 向量语义检索"""

    def __init__(self):
        self.settings = get_settings()
        self.embedder = Embedder()
        self.bm25 = BM25Retriever()
        self.storage = StorageManager(self.settings.cache_dir)
        self._documents: List[Document] = []
        self._doc_map: Dict[str, Document] = {}  # file_path -> Document
        self._embeddings: Dict[str, List[float]] = {}  # file_path -> vector
        self._initialized = False

    def initialize(self) -> None:
        """
        初始化检索器：
        1. 解析所有文档
        2. 检查缓存是否存在且有效
        3. 需要更新的文档重新计算embedding和BM25索引
        4. 持久化更新后的缓存
        """
        # 1. 解析所有文档
        self._documents = parse_all_documents(self.settings.memory_root_dir)
        self._doc_map = {doc.file_path: doc for doc in self._documents}

        # 2. 尝试从缓存加载
        cached_embeddings = self.storage.load_embeddings()
        cached_bm25 = self.storage.load_bm25_corpus()

        if cached_embeddings is not None:
            self._embeddings = cached_embeddings

        if cached_bm25 is not None:
            self.bm25.load_from_cache(
                corpus=cached_bm25["corpus"],
                file_paths=cached_bm25["file_paths"],
            )

        # 3. 检查哪些文档需要更新
        all_file_paths = [doc.file_path for doc in self._documents]
        # storage.needs_update 需要绝对路径来检测mtime，这里用相对路径构建绝对路径
        from pathlib import Path
        memory_root = Path(self.settings.memory_root_dir).resolve()
        abs_paths = [str(memory_root / fp) for fp in all_file_paths]
        needs_update_abs = self.storage.needs_update(abs_paths)

        # 转换回相对路径集合
        needs_update_rel = set()
        for abs_path in needs_update_abs:
            try:
                rel = str(Path(abs_path).relative_to(memory_root)).replace("\\", "/")
                needs_update_rel.add(rel)
            except ValueError:
                pass

        # 如果全部都需要更新（首次运行），或者有增量更新
        need_rebuild_bm25 = len(needs_update_rel) > 0 or cached_bm25 is None

        # 4. 对需要更新的文档计算embedding
        if needs_update_rel:
            docs_to_embed = [
                doc for doc in self._documents if doc.file_path in needs_update_rel
            ]
            texts = [doc.content for doc in docs_to_embed]

            if texts:
                embeddings = self.embedder.embed_texts(texts)
                for doc, emb in zip(docs_to_embed, embeddings):
                    self._embeddings[doc.file_path] = emb

        # 移除已不存在的文档的embedding
        current_paths = set(all_file_paths)
        removed_paths = [p for p in self._embeddings if p not in current_paths]
        for p in removed_paths:
            del self._embeddings[p]

        # 5. 重建BM25索引（如果有变化）
        if need_rebuild_bm25:
            bm25_docs = [
                {"content": doc.content, "file_path": doc.file_path}
                for doc in self._documents
            ]
            self.bm25.build_index(bm25_docs)

        # 6. 持久化
        self.storage.save_embeddings(self._embeddings)
        corpus, file_paths = self.bm25.get_corpus()
        self.storage.save_bm25_corpus(corpus, file_paths)

        # 保存文件mtime
        abs_mtime_map = self.storage.get_file_mtimes(abs_paths)
        self.storage.save_file_mtimes(abs_mtime_map)

        self._initialized = True

    def _vector_search(self, query: str, top_k: int) -> List[Tuple[str, float]]:
        """
        向量语义检索：
        1. 将query向量化
        2. 计算与所有文档向量的余弦相似度
        3. 取top_k
        返回: [(file_path, similarity_score), ...]
        """
        if not self._embeddings:
            return []

        query_vector = np.array(self.embedder.embed_query(query))
        query_norm = np.linalg.norm(query_vector)
        if query_norm == 0:
            return []

        scores: List[Tuple[str, float]] = []
        for file_path, doc_vector in self._embeddings.items():
            doc_vec = np.array(doc_vector)
            doc_norm = np.linalg.norm(doc_vec)
            if doc_norm == 0:
                continue
            cosine_sim = float(np.dot(query_vector, doc_vec) / (query_norm * doc_norm))
            scores.append((file_path, cosine_sim))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]

    def _normalize_scores(self, scores: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
        """
        Min-Max归一化分数到[0,1]区间。
        处理边界情况：所有分数相同时返回均匀值。
        """
        if not scores:
            return []

        values = [s for _, s in scores]
        min_val = min(values)
        max_val = max(values)

        # 边界情况：所有分数相同
        if max_val == min_val:
            return [(path, 1.0) for path, _ in scores]

        return [
            (path, (score - min_val) / (max_val - min_val))
            for path, score in scores
        ]

    def hybrid_search(self, query: str, top_k: Optional[int] = None) -> List[Tuple[Document, float]]:
        """
        混合检索：
        1. BM25检索 → 归一化分数
        2. 向量检索 → 归一化分数
        3. 加权融合: final_score = vector_weight * vector_score + bm25_weight * bm25_score
        4. 合并去重，按融合分数降序排列
        5. 返回top_k个 (Document, score)
        """
        if not self._initialized:
            self.initialize()

        if top_k is None:
            top_k = self.settings.top_k

        # 扩大检索范围以获得更好的融合效果
        search_k = top_k * 3

        # 1. BM25检索并归一化
        bm25_results = self.bm25.search(query, top_k=search_k)
        bm25_normalized = self._normalize_scores(bm25_results)
        bm25_scores: Dict[str, float] = {path: score for path, score in bm25_normalized}

        # 2. 向量检索并归一化
        vector_results = self._vector_search(query, top_k=search_k)
        vector_normalized = self._normalize_scores(vector_results)
        vector_scores: Dict[str, float] = {path: score for path, score in vector_normalized}

        # 3. 融合分数
        all_paths = set(bm25_scores.keys()) | set(vector_scores.keys())
        fused_scores: List[Tuple[str, float]] = []

        for path in all_paths:
            v_score = vector_scores.get(path, 0.0)
            b_score = bm25_scores.get(path, 0.0)
            final_score = (
                self.settings.vector_weight * v_score
                + self.settings.bm25_weight * b_score
            )
            fused_scores.append((path, final_score))

        # 4. 按融合分数降序排列
        fused_scores.sort(key=lambda x: x[1], reverse=True)

        # 5. 返回top_k个结果
        results: List[Tuple[Document, float]] = []
        for path, score in fused_scores[:top_k]:
            doc = self._doc_map.get(path)
            if doc is not None:
                results.append((doc, score))

        return results

    def get_document(self, file_path: str) -> Optional[Document]:
        """根据文件路径获取文档"""
        return self._doc_map.get(file_path)
