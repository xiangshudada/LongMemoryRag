服务:content-service
版本:v1
路径:POST /api/content/comment/create
描述:创建评论
请求参数:
- articleId: integer, 必填, 文章ID
- userId: integer, 必填, 用户ID
- content: string, 必填, 评论内容

请求体:
```json
{"articleId": 1001, "userId": 123, "content": "很好的文章!"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"commentId": 2001}}
```

错误码:
- 5003: 文章不存在
- 5002: 用户不存在
- 5005: 评论内容为空
