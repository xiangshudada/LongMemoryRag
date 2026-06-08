# 中台接口 RAG 问答系统

基于本地 Markdown 知识库的中台接口智能问答系统。通过 BM25 + 向量语义混合检索，对接阿里百炼大模型，实现对 100+ 微服务 API 文档的自然语言查询。

## 核心特性

- **阿里百炼 text-embedding-v4** 语义向量化
- **BM25 + 向量混合检索**（jieba 中文分词 + 余弦相似度）
- **LangGraph 工作流编排**（条件路由，按需检索）
- **本地 JSON 持久化**（无需向量数据库，增量更新缓存）
- **只读模式**，用户仅可查询，不可修改知识库

## 技术栈

| 组件 | 技术 |
|------|------|
| 工作流编排 | LangGraph >= 0.2.0 |
| LLM 框架 | LangChain >= 0.3.0 |
| 大模型 | 阿里百炼 qwen-plus |
| Embedding | dashscope text-embedding-v4 |
| 关键词检索 | rank-bm25 + jieba |
| 数值计算 | numpy |
| 配置管理 | pydantic-settings |

## 项目结构

```
RagAgent/
├── main.py                  # 入口，交互式 CLI
├── pyproject.toml           # 项目配置与依赖
├── .env.example             # 环境变量模板
├── src/
│   ├── config.py            # pydantic-settings 配置加载
│   ├── parser.py            # Markdown 文档解析
│   ├── embedder.py          # dashscope embedding 封装
│   ├── bm25.py              # BM25 检索（jieba 分词）
│   ├── retriever.py         # 混合检索器（BM25 + 向量融合）
│   └── storage.py           # JSON 持久化（缓存管理）
├── agents/
│   ├── state.py             # LangGraph 状态定义
│   ├── nodes.py             # 工作流节点（理解/检索/生成）
│   └── graph.py             # LangGraph 工作流构建
├── memory/                  # 知识库（Markdown API 文档）
│   ├── knowledge_index.md   # 知识索引
│   └── api_docs/            # 7 个微服务接口文档
└── .cache/                  # 本地持久化缓存（自动生成）
```

## 快速开始

### 环境要求

- Python >= 3.10
- 阿里百炼 API Key（[获取地址](https://dashscope.console.aliyun.com/)）

### 安装依赖

```bash
# 方式一：editable 安装
pip install -e .

# 方式二：直接安装依赖
pip install langgraph langchain langchain-openai dashscope numpy rank-bm25 jieba pydantic pydantic-settings
```

### 配置

```bash
cp .env.example .env
```

编辑 `.env`，填入你的 API Key：

```env
DASHSCOPE_API_KEY=sk-xxxxxxxxxxxxxxxx
```

### 运行

```bash
.venv\Scripts\python.exe main.py
```

首次运行会自动解析知识库并构建索引缓存，后续启动为增量更新。

## 配置说明

| 环境变量 | 说明 | 默认值 |
|----------|------|--------|
| `DASHSCOPE_API_KEY` | 阿里百炼 API 密钥 | （必填） |
| `LLM_MODEL` | 大模型名称 | `qwen-plus` |
| `EMBEDDING_MODEL` | Embedding 模型 | `text-embedding-v4` |
| `MEMORY_ROOT_DIR` | 知识库根目录 | `./memory` |
| `CACHE_DIR` | 缓存存储目录 | `./.cache` |
| `TOP_K` | 检索返回文档数 | `5` |
| `VECTOR_WEIGHT` | 向量检索权重 | `0.6` |
| `BM25_WEIGHT` | BM25 检索权重 | `0.4` |

## 架构说明

### LangGraph 工作流

```
START → query_understanding → [条件路由]
                                ├─ 需要检索 → retrieve → generate → END
                                └─ 直接回答 → generate → END
```

- **query_understanding**：分析用户意图，判断是否需要检索知识库
- **retrieve**：执行混合检索，获取相关文档
- **generate**：基于检索结果（或直接）生成回答

### 混合检索流程

```
用户查询
  │
  ├──→ BM25 检索（jieba 分词 → 关键词匹配）──→ 归一化 ──┐
  │                                                       │
  └──→ 向量检索（embedding → 余弦相似度）──→ 归一化 ──────┤
                                                          │
                                            加权融合 ←────┘
                                    (向量 × 0.6 + BM25 × 0.4)
                                              │
                                         Top-K 排序
                                              │
                                         返回文档
```

## 知识库

`memory/api_docs/` 目录包含 7 个微服务的接口文档：

| 服务 | 说明 |
|------|------|
| user_service | 用户服务（v1/v2 版本化管理） |
| order_service | 订单服务 |
| payment_service | 支付服务 |
| product_service | 商品服务 |
| content_service | 内容服务 |
| notification_service | 通知服务 |
| system_service | 系统管理服务 |

共计 100+ 接口文档，每个文档为标准 Markdown 格式，包含接口路径、请求参数、响应示例等。

## 使用示例

```
Q: 如何创建订单？
A: 创建订单使用 POST /api/order/create 接口，需要传入商品ID、数量、收货地址等参数...

Q: 用户登录接口的请求参数是什么？
A: 用户登录接口 POST /api/user/login 需要以下参数：username(用户名)、password(密码)...

Q: 支付服务支持哪些操作？
A: 支付服务提供以下接口：创建支付、查询支付状态、退款、提现、充值、账户绑定...
```
