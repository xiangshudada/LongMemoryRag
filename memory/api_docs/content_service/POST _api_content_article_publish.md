服务:content-service
版本:v1
路径:POST /api/content/article/publish
描述:发布文章
请求参数:
- articleId: integer, 必填, 文章ID

请求体:
```json
{"articleId": 1001}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"articleId": 1001, "status": "published", "publishedAt": "2024-01-01T00:00:00Z"}}
```

错误码:
- 5003: 文章不存在
- 5010: 文章已发布
