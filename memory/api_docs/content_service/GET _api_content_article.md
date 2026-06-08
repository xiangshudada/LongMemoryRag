服务:content-service
版本:v1
路径:GET /api/content/article/{articleId}
描述:获取文章详情
请求参数:
- articleId: integer, 必填, 文章ID

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"articleId": 1001, "title": "测试文章", "content": "文章内容...", "authorId": 123, "views": 1000}}
```

错误码:
- 5003: 文章不存在
