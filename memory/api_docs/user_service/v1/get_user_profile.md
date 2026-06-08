服务:user-service
版本:v1
路径:GET /api/user/{userId}/profile
描述:获取用户完整资料
请求参数:
- userId: integer, 必填, 用户ID

请求体:
无

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "userId": 123,
    "username": "testuser",
    "phone": "13800138000",
    "email": "test@example.com",
    "avatar": "https://cdn.example.com/avatars/123.jpg",
    "bio": "个人简介",
    "gender": "male",
    "birthday": "1990-01-01",
    "createdAt": "2024-01-01T00:00:00Z"
  }
}
```

错误码:
- 1003: 用户不存在
