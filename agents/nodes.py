import re
from typing import Optional

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from src.retriever import HybridRetriever
from src.config import get_settings
from agents.state import AgentState

# 全局检索器实例（在main.py中初始化后注入）
_retriever: Optional[HybridRetriever] = None

# API相关关键词集合
_API_KEYWORDS = {
    "接口", "API", "api", "服务", "参数", "请求", "响应", "路径", "版本",
    "登录", "注册", "创建", "查询", "删除", "修改", "支付", "订单", "用户",
    "商品", "通知", "上传", "下载", "导出", "退款", "充值", "提现",
    "收藏", "关注", "评论", "点赞", "搜索", "列表", "详情",
    "密码", "头像", "权限", "角色", "配置", "日志", "备份",
    "分类", "库存", "状态", "发货", "确认", "取消",
    "文章", "内容", "发布", "模板", "推送", "邮件", "短信",
    "系统", "健康", "监控", "缓存", "维护", "公告",
    "token", "鉴权", "认证", "授权",
    "GET", "POST", "PUT", "DELETE", "PATCH",
    "endpoint", "url", "method", "header", "body",
}


def set_retriever(retriever: HybridRetriever):
    """注入检索器实例"""
    global _retriever
    _retriever = retriever


def query_understanding_node(state: AgentState) -> dict:
    """
    查询理解节点：判断用户问题是否需要检索API文档。

    规则：
    - 包含API相关关键词 → need_retrieval=True
    - 闲聊/问候/无关问题 → need_retrieval=False
    """
    query = state["query"]

    # 检查是否包含API相关关键词
    for keyword in _API_KEYWORDS:
        if keyword in query:
            return {"need_retrieval": True}

    return {"need_retrieval": False}


def retrieve_node(state: AgentState) -> dict:
    """
    检索节点：调用HybridRetriever执行混合检索。
    返回检索到的文档列表。
    """
    if _retriever is None:
        return {"documents": []}

    query = state["query"]
    results = _retriever.hybrid_search(query)
    return {"documents": results}


def _format_documents(documents: list) -> str:
    """格式化检索结果为可读文本"""
    if not documents:
        return ""

    formatted_parts = []
    for i, (doc, score) in enumerate(documents, 1):
        meta = doc.metadata
        service = meta.get("service", "未知服务")
        version = meta.get("version", "")
        method = meta.get("method", "")
        path = meta.get("path", "")
        description = meta.get("description", "")

        header = f"### 文档 {i} (相关度: {score:.2f})"
        info_parts = [f"- 服务: {service}"]
        if version:
            info_parts.append(f"- 版本: {version}")
        if method and path:
            info_parts.append(f"- 接口: {method} {path}")
        elif path:
            info_parts.append(f"- 路径: {path}")
        if description:
            info_parts.append(f"- 描述: {description}")

        # 截取内容摘要（最多前500字符）
        content_preview = doc.content[:500]
        if len(doc.content) > 500:
            content_preview += "..."

        info_parts.append(f"- 内容:\n{content_preview}")
        formatted_parts.append(f"{header}\n" + "\n".join(info_parts))

    return "\n\n".join(formatted_parts)


def generate_node(state: AgentState) -> dict:
    """
    生成节点：调用 qwen-plus 基于检索结果生成回答。
    """
    settings = get_settings()

    llm = ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.dashscope_api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    query = state["query"]
    need_retrieval = state["need_retrieval"]
    documents = state["documents"]

    if need_retrieval and documents:
        # 有检索结果
        formatted_docs = _format_documents(documents)
        system_msg = (
            "你是一个中台API文档助手。请根据以下检索到的API文档内容，准确回答用户的问题。"
            "如果检索结果中没有相关信息，请如实告知。回答时请引用具体的接口路径和参数信息。"
        )
        user_msg = f"## 检索到的文档：\n{formatted_docs}\n\n## 用户问题：\n{query}"
    elif need_retrieval and not documents:
        # 需要检索但无结果
        system_msg = (
            "你是一个中台API文档助手。未能找到与用户问题相关的API文档。请告知用户可以查询的范围包括："
            "用户服务、订单服务、支付服务、商品服务、内容服务、系统服务、通知服务。"
        )
        user_msg = query
    else:
        # 不需要检索（闲聊）
        system_msg = "你是一个中台API文档助手。用户的问题不涉及API文档，请友好地回应。"
        user_msg = query

    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=user_msg),
    ]

    response = llm.invoke(messages)
    return {"answer": response.content}


def should_retrieve(state: AgentState) -> str:
    """条件路由：根据 need_retrieval 决定下一步"""
    if state["need_retrieval"]:
        return "retrieve"
    return "generate"
