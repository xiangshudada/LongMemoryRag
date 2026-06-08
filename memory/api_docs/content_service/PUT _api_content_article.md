服务:content-service
版本:v1
路径:PUT /api/content/article/{articleId}
描述:更新文章
请求参数:
- articleId: integer, 必填, 文章ID

请求体:
```json
{"title": "新标题", "content": "新内容..."}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"articleId": 1001}}
```

错误码:
- 5003: 文章不存在
- 5004: 无权限修改
