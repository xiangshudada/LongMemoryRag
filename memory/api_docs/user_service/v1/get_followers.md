服务:user-service
版本:v1
路径:GET /api/user/{userId}/followers
描述:获取粉丝列表
请求参数:
- userId: integer, 必填, 用户ID
- page: integer, 必填, 页码
- pageSize: integer, 必填, 每页数量

请求体:
无

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "total": 500,
    "items": [
      {"userId": 456, "username": "fan1", "avatar": "url"}
    ]
  }
}
```

错误码:
- 1003: 用户不存在
