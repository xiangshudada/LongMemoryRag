import jieba
from typing import List, Optional, Tuple

from rank_bm25 import BM25Okapi


# 常见中文停用词
STOP_WORDS = frozenset([
    "的", "了", "是", "在", "和", "与", "或", "不", "有", "也",
    "就", "都", "而", "及", "着", "把", "被", "让", "给", "到",
    "从", "上", "下", "中", "来", "去", "过", "对", "可", "能",
    "会", "要", "将", "已", "还", "为", "以", "所", "这", "那",
    "之", "等", "如", "但", "又", "很", "更", "最", "其", "该",
    "个", "各", "些", "么", "什", "吗", "吧", "呢", "啊",
    "一", "二", "三", "四", "五", "六", "七", "八", "九", "十",
    "用", "使", "使用", "进行", "通过", "可以", "需要", "支持",
])


class BM25Retriever:
    """BM25关键词检索器"""

    def __init__(self):
        self._index: Optional[BM25Okapi] = None
        self._corpus: List[List[str]] = []  # 分词后的语料库
        self._file_paths: List[str] = []    # 对应的文件路径

    def tokenize(self, text: str) -> List[str]:
        """
        中文分词：使用jieba搜索引擎模式分词，过滤停用词和单字符词。
        """
        words = jieba.cut_for_search(text)
        return [
            w.strip()
            for w in words
            if w.strip() and len(w.strip()) > 1 and w.strip() not in STOP_WORDS
        ]

    def build_index(self, documents: List[dict]) -> None:
        """
        构建BM25索引。
        documents: [{"content": "...", "file_path": "..."}, ...]
        """
        self._corpus = []
        self._file_paths = []

        for doc in documents:
            tokens = self.tokenize(doc["content"])
            self._corpus.append(tokens)
            self._file_paths.append(doc["file_path"])

        if self._corpus:
            self._index = BM25Okapi(self._corpus)
        else:
            self._index = None

    def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """
        BM25检索。
        返回: [(file_path, score), ...] 按分数降序排列
        """
        if self._index is None or not self._corpus:
            return []

        tokenized_query = self.tokenize(query)
        if not tokenized_query:
            return []

        scores = self._index.get_scores(tokenized_query)

        # 获取top_k个最高分的索引
        scored_docs = [
            (self._file_paths[i], float(scores[i]))
            for i in range(len(scores))
            if scores[i] > 0
        ]
        scored_docs.sort(key=lambda x: x[1], reverse=True)

        return scored_docs[:top_k]

    def load_from_cache(self, corpus: List[List[str]], file_paths: List[str]) -> None:
        """从缓存加载索引"""
        self._corpus = corpus
        self._file_paths = file_paths
        if self._corpus:
            self._index = BM25Okapi(self._corpus)
        else:
            self._index = None

    def get_corpus(self) -> Tuple[List[List[str]], List[str]]:
        """获取语料库和文件路径（用于持久化）"""
        return self._corpus, self._file_paths
