import hashlib
from typing import Dict, List, Optional

from dashscope import TextEmbedding

from src.config import get_settings


class Embedder:
    """阿里百炼 text-embedding-v4 向量化器"""

    BATCH_SIZE = 10  # dashscope text-embedding-v4 单次最多支持10条文本

    def __init__(self):
        self.settings = get_settings()
        self._cache: Dict[str, List[float]] = {}  # key: text hash -> embedding

    @staticmethod
    def _hash_text(text: str) -> str:
        """计算文本的SHA256哈希作为缓存key"""
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        批量向量化文本。
        dashscope TextEmbedding.call 单次最多支持10条文本，需要分批调用。
        使用内存缓存避免重复计算。
        """
        if not texts:
            return []

        results: List[Optional[List[float]]] = [None] * len(texts)
        uncached_indices: List[int] = []

        # 先查缓存
        for i, text in enumerate(texts):
            text_hash = self._hash_text(text)
            if text_hash in self._cache:
                results[i] = self._cache[text_hash]
            else:
                uncached_indices.append(i)

        # 对未缓存的文本分批调用API
        if uncached_indices:
            uncached_texts = [texts[i] for i in uncached_indices]

            for batch_start in range(0, len(uncached_texts), self.BATCH_SIZE):
                batch = uncached_texts[batch_start:batch_start + self.BATCH_SIZE]
                batch_indices = uncached_indices[batch_start:batch_start + self.BATCH_SIZE]

                response = TextEmbedding.call(
                    model=self.settings.embedding_model,
                    input=batch,
                    api_key=self.settings.dashscope_api_key,
                )

                if response.status_code != 200:
                    raise RuntimeError(
                        f"Embedding API调用失败: status_code={response.status_code}, "
                        f"message={response.message}"
                    )

                # response.output['embeddings'] 是 [{"text_index": 0, "embedding": [...]}, ...]
                embeddings_output = response.output["embeddings"]
                # 按 text_index 排序确保顺序正确
                embeddings_output.sort(key=lambda x: x["text_index"])

                for j, emb_item in enumerate(embeddings_output):
                    embedding = emb_item["embedding"]
                    original_idx = batch_indices[j]
                    results[original_idx] = embedding
                    # 写入缓存
                    text_hash = self._hash_text(texts[original_idx])
                    self._cache[text_hash] = embedding

        return results  # type: ignore

    def embed_query(self, query: str) -> List[float]:
        """单条查询向量化"""
        result = self.embed_texts([query])
        return result[0]

    def load_cache(self, cache: Dict[str, List[float]]) -> None:
        """从持久化加载缓存"""
        self._cache.update(cache)

    def get_cache(self) -> Dict[str, List[float]]:
        """获取当前缓存（用于持久化）"""
        return dict(self._cache)
