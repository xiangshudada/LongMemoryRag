import sys

from src.config import get_settings
from src.retriever import HybridRetriever
from agents.nodes import set_retriever
from agents.graph import build_graph


def main():
    """
    主入口：
    1. pydantic-settings自动从.env读取环境变量
    2. 初始化HybridRetriever（首次运行自动构建索引）
    3. 构建LangGraph工作流
    4. 进入交互式CLI循环
    """
    print("=" * 50)
    print("  中台接口 RAG 问答系统")
    print("  (输入 'quit' 或 'exit' 退出)")
    print("=" * 50)

    # 初始化
    print("\n正在初始化检索器...")
    try:
        settings = get_settings()
    except Exception as e:
        print(f"配置加载失败，请检查 .env 文件: {e}")
        sys.exit(1)

    retriever = HybridRetriever()
    retriever.initialize()
    print(f"检索器初始化完成，已索引 {len(retriever._documents)} 个文档")

    # 注入检索器并构建图
    set_retriever(retriever)
    graph = build_graph()

    print("\n系统就绪，请输入您的问题：\n")

    # 交互循环
    while True:
        try:
            query = input("Q: ").strip()
            if not query:
                continue
            if query.lower() in ("quit", "exit", "q"):
                print("再见！")
                break

            # 执行工作流
            result = graph.invoke({
                "query": query,
                "need_retrieval": False,
                "documents": [],
                "answer": "",
            })
            print(f"\nA: {result['answer']}\n")
            print("-" * 50)

        except KeyboardInterrupt:
            print("\n再见！")
            break
        except Exception as e:
            print(f"\n处理出错: {e}\n")


if __name__ == "__main__":
    main()
