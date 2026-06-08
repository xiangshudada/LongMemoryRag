from typing import TypedDict, List
from src.parser import Document


class AgentState(TypedDict):
    """LangGraph 工作流状态"""
    query: str                              # 用户原始查询
    need_retrieval: bool                    # 是否需要检索
    documents: List[tuple]                  # 检索结果 [(Document, score), ...]
    answer: str                             # 最终回答
