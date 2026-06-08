import json
import os
from typing import Dict, List, Optional
from pathlib import Path


class StorageManager:
    """本地JSON文件持久化管理器"""

    def __init__(self, cache_dir: str = "./.cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_path(self, filename: str) -> Path:
        """获取缓存文件的完整路径"""
        return self.cache_dir / filename

    def _save_json(self, filename: str, data) -> None:
        """通用JSON保存方法"""
        file_path = self._get_path(filename)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _load_json(self, filename: str):
        """通用JSON加载方法，文件不存在返回None"""
        file_path = self._get_path(filename)
        if not file_path.exists():
            return None
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_embeddings(self, embeddings: Dict[str, List[float]]) -> None:
        """保存向量缓存 {file_path: vector}"""
        self._save_json("embeddings.json", embeddings)

    def load_embeddings(self) -> Optional[Dict[str, List[float]]]:
        """加载向量缓存，不存在则返回None"""
        return self._load_json("embeddings.json")

    def save_bm25_corpus(self, corpus: List[List[str]], file_paths: List[str]) -> None:
        """保存BM25分词语料库和对应文件路径"""
        data = {
            "corpus": corpus,
            "file_paths": file_paths,
        }
        self._save_json("bm25_index.json", data)

    def load_bm25_corpus(self) -> Optional[dict]:
        """加载BM25语料库，返回 {corpus, file_paths}"""
        return self._load_json("bm25_index.json")

    def save_documents_meta(self, documents_meta: List[dict]) -> None:
        """保存文档元数据列表（用于快速重建索引）"""
        self._save_json("documents_meta.json", documents_meta)

    def load_documents_meta(self) -> Optional[List[dict]]:
        """加载文档元数据"""
        return self._load_json("documents_meta.json")

    def get_file_mtimes(self, file_paths: List[str]) -> Dict[str, float]:
        """获取文件修改时间，用于增量更新判断"""
        mtimes = {}
        for fp in file_paths:
            try:
                mtimes[fp] = os.path.getmtime(fp)
            except OSError:
                # 文件不存在或无法访问
                pass
        return mtimes

    def save_file_mtimes(self, mtimes: Dict[str, float]) -> None:
        """保存文件修改时间"""
        self._save_json("file_mtimes.json", mtimes)

    def load_file_mtimes(self) -> Optional[Dict[str, float]]:
        """加载已保存的文件修改时间"""
        return self._load_json("file_mtimes.json")

    def needs_update(self, file_paths: List[str]) -> List[str]:
        """
        判断哪些文件需要重新索引（新增或修改）。
        对比当前文件mtime与已保存的mtime。
        """
        saved_mtimes = self.load_file_mtimes()

        # 如果没有保存过，则所有文件都需要更新
        if saved_mtimes is None:
            return file_paths

        needs = []
        for fp in file_paths:
            # 新文件（之前没有记录）
            if fp not in saved_mtimes:
                needs.append(fp)
                continue
            # 检查文件是否被修改
            try:
                current_mtime = os.path.getmtime(fp)
                if current_mtime > saved_mtimes[fp]:
                    needs.append(fp)
            except OSError:
                # 文件无法访问，跳过
                pass

        return needs
