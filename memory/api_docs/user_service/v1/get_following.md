服务:user-service
版本:v1
路径:GET /api/user/{userId}/following
描述:获取关注列表
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
    "total": 200,
    "items": [
      {"userId": 789, "username": "user1", "avatar": "url"}
    ]
  }
}
```

错误码:
- 1003: 用户不存在
