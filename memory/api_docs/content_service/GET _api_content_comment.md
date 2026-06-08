服务:content-service
版本:v1
路径:GET /api/content/comment/{articleId}
描述:获取文章评论
请求参数:
- articleId: integer, 必填, 文章ID
- page: integer, 必填, 页码
- pageSize: integer, 必填, 每页数量

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"total": 50, "items": [{"commentId": 2001, "content": "很好的文章!", "userId": 123}]}}
```

错误码:
- 5003: 文章不存在
