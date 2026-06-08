# 记忆文件目录结构

## 概览
- **接口文件总数**: 100个
- **服务数量**: 7个
- **知识库类型**: API 文档库
- **目录结构**: 支持多层嵌套和分层索引

## 目录结构

```
memory/
├── knowledge_index.md                    # 顶层索引 (知识库级)
├── README.md                             # 本文件
└── api_docs/                             # API 文档库
    ├── _index.md                         # API文档库索引
    ├── user_service/                     # 用户服务 (15个接口)
    │   ├── _index.md                     # 服务级索引
    │   └── ...接口文件
    ├── order_service/                    # 订单服务 (15个接口)
    │   ├── _index.md
    │   └── ...接口文件
    ├── payment_service/                  # 支付服务 (14个接口)
    │   ├── _index.md
    │   └── ...接口文件
    ├── product_service/                  # 商品服务 (14个接口)
    │   ├── _index.md
    │   └── ...接口文件
    ├── content_service/                  # 内容服务 (14个接口)
    │   ├── _index.md
    │   └── ...接口文件
    ├── system_service/                   # 系统服务 (15个接口)
    │   ├── _index.md
    │   └── ...接口文件
    └── notification_service/             # 通知服务 (13个接口)
        ├── _index.md
        └── ...接口文件
```

## 服务统计

| 服务名称 | 版本 | 接口数量 | 主要功能 |
|---------|------|---------|---------|
| user-service | v1 | 15 | 用户管理、认证、资料、社交关系 |
| order-service | v1 | 15 | 订单全生命周期管理 |
| payment-service | v2 | 14 | 支付、退款、提现、充值、分账 |
| product-service | v1 | 14 | 商品管理、库存、分类、评价 |
| content-service | v1 | 14 | 文章、评论、点赞、文件管理 |
| system-service | v1 | 15 | 系统配置、监控、备份、权限 |
| notification-service | v1 | 13 | 短信、邮件、推送、Webhook |
| **总计** | - | **100** | - |

## 接口类型分布

- **POST**: 55个 (创建、更新、操作类接口)
- **GET**: 35个 (查询、列表、详情类接口)
- **PUT**: 7个 (更新类接口)
- **DELETE**: 3个 (删除类接口)

## 如何使用

### 1. 添加新记忆
在对应服务目录下创建新的 `.md` 文件,按照标准格式编写即可。

### 2. 更新索引
编辑 `knowledge_index.md`,添加新的索引条目。

### 3. 系统自动加载
RAG 系统会在查询时自动按需加载所有记忆文件。

## 记忆文件格式

每个接口记忆文件遵循以下格式:

```markdown
服务:service-name
版本:vx
路径:HTTP_METHOD /api/path
描述:接口描述
请求参数:
- param1: type, 必填/可选, 说明
- param2: type, 必填/可选, 说明

请求体:
```json
{...}
```

响应体:
```json
{...}
```

错误码:
- 1001: 错误描述
- 1002: 错误描述
```

## 生成工具

使用 `generate_apis.py` 脚本可以批量生成接口记忆文件:

```bash
python generate_apis.py
```

该脚本会根据预定义的接口数据自动生成格式化的记忆文件。
