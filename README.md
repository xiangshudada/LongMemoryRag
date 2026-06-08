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

## 缓存管理策略

### 缓存目录结构

```
.cache/
├── embeddings.json      # 文档向量缓存 (file_path -> vector)
├── bm25_index.json      # BM25 分词语料库索引
└── file_mtimes.json     # 文件修改时间戳（用于增量更新）
```

### 缓存工作流程

1. **初始化加载**：启动时从 `.cache` 加载已存在的缓存
2. **增量更新**：通过对比文件修改时间（mtime），只更新变化的文档
3. **孤儿清理**：删除已不存在文档对应的缓存条目
4. **持久化保存**：每次更新后立即保存到 JSON 文件

### 缓存策略优势

- ✅ **节省 API 成本**：避免重复调用 Embedding API
- ✅ **快速启动**：增量更新机制，只处理变化的文档
- ✅ **自动管理**：首次运行自动构建，后续自动更新
- ✅ **无需数据库**：纯本地文件存储，零依赖

### ⚠️ 已知风险与限制

#### 🔴 高风险

1. **缓存无限增长**
   - **问题**：`embeddings.json` 只增不减，没有大小限制
   - **影响**：长期运行后文件可能达到数百 MB
   - **场景**：文档频繁更新、大量历史文档累积
   - **建议**：定期清理 `.cache` 目录或实现 LRU 淘汰策略

2. **并发写入冲突**
   - **问题**：多进程同时写入缓存文件无锁保护
   - **影响**：可能导致 JSON 文件损坏
   - **场景**：多实例部署、并行初始化
   - **建议**：添加文件锁或使用原子写入（临时文件 + rename）

3. **缓存损坏无恢复**
   - **问题**：JSON 文件损坏时直接抛异常，系统无法启动
   - **影响**：服务不可用，需手动删除缓存
   - **场景**：异常退出、磁盘满、文件损坏
   - **建议**：添加 JSON 校验和损坏自动重建机制

#### 🟡 中风险

4. **模型版本不兼容**
   - **问题**：缓存未记录 embedding 模型版本
   - **影响**：切换模型后使用旧向量导致检索质量下降
   - **场景**：升级 text-embedding-v4 到 v5
   - **建议**：在缓存元数据中记录模型名称和版本

5. **内存缓存泄漏**
   - **问题**：`Embedder._cache` 字典无限增长（`embedder.py:16`）
   - **影响**：长时间运行后内存占用持续增长
   - **场景**：高频查询不同问题
   - **建议**：设置最大缓存条目数（如 10000 条），使用 LRU 策略

6. **mtime 精度问题**
   - **问题**：某些文件系统 mtime 精度为秒级
   - **影响**：快速修改可能检测不到变化
   - **场景**：自动化脚本批量更新文档
   - **建议**：结合文件大小 + mtime + hash 综合判断

#### 🟢 低风险

7. **缓存统计缺失**
   - **问题**：无缓存命中率、大小、条目数等指标
   - **影响**：无法监控缓存效果和性能
   - **建议**：添加缓存统计接口和日志

8. **Windows 路径分隔符**
   - **问题**：相对路径使用 `/`，但 Windows 使用 `\`
   - **影响**：路径匹配可能失败（代码已处理，但需持续验证）
   - **场景**：跨平台部署
   - **状态**：当前代码已通过 `replace("\\", "/")` 处理

### 缓存清理建议

```bash
# 方式一：完全重建（推荐在模型升级或缓存异常时使用）
rm -rf .cache/
python main.py  # 自动重建

# 方式二：定期清理（Linux/Mac）
find .cache/ -name "*.json" -mtime +30 -delete

# 方式三：Windows PowerShell
Get-ChildItem .cache\*.json | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } | Remove-Item
```

### 监控建议

定期检查缓存状态：

```python
import os
from pathlib import Path

cache_dir = Path("./.cache")
for f in cache_dir.glob("*.json"):
    size_mb = f.stat().st_size / (1024 * 1024)
    print(f"{f.name}: {size_mb:.2f} MB")
```

**告警阈值**：
- 单个文件 > 50 MB：需要关注
- 单个文件 > 100 MB：建议清理
- 总缓存 > 200 MB：必须清理

## 使用示例

```
Q: 如何创建订单？
A: 创建订单使用 POST /api/order/create 接口，需要传入商品ID、数量、收货地址等参数...

Q: 用户登录接口的请求参数是什么？
A: 用户登录接口 POST /api/user/login 需要以下参数：username(用户名)、password(密码)...

Q: 支付服务支持哪些操作？
A: 支付服务提供以下接口：创建支付、查询支付状态、退款、提现、充值、账户绑定...
```
