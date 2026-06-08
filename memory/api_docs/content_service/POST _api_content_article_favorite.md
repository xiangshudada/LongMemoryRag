服务:content-service
版本:v1
路径:POST /api/content/article/favorite
描述:收藏文章
请求参数:
- articleId: integer, 必填, 文章ID
- userId: integer, 必填, 用户ID

请求体:
```json
{
  "articleId": 1001,
  "userId": 123
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "favoriteId": 5001
  }
}
```

错误码:
- 5003: 文章不存在
- 5011: 已收藏
