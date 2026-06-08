服务:user-service
版本:v1
路径:GET /api/user/{userId}
描述:获取用户详情
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
    "createdAt": "2024-01-01T00:00:00Z"
  }
}
```

错误码:
- 1003: 用户不存在
- 1004: 无权访问
