from langgraph.graph import StateGraph, END
from agents.state import AgentState
from agents.nodes import (
    query_understanding_node,
    retrieve_node,
    generate_node,
    should_retrieve,
)


def build_graph():
    """
    构建 LangGraph RAG 工作流：

    START → query_understanding → [条件路由]
                                    ├─ "retrieve" → retrieve → generate → END
                                    └─ "generate" → generate → END
    """
    workflow = StateGraph(AgentState)

    # 添加节点
    workflow.add_node("query_understanding", query_understanding_node)
    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("generate", generate_node)

    # 设置入口
    workflow.set_entry_point("query_understanding")

    # 条件边
    workflow.add_conditional_edges(
        "query_understanding",
        should_retrieve,
        {
            "retrieve": "retrieve",
            "generate": "generate",
        },
    )

    # 普通边
    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile()
