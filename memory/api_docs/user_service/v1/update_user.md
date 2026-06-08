服务:user-service
版本:v1
路径:PUT /api/user/{userId}
描述:更新用户信息
请求参数:
- userId: integer, 必填, 用户ID
- username: string, 可选, 用户名
- phone: string, 可选, 手机号
- email: string, 可选, 邮箱

请求体:
```json
{
  "username": "newname",
  "phone": "13900139000",
  "email": "new@example.com"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": { "userId": 123 }
}
```

错误码:
- 1003: 用户不存在
- 1002: 参数错误
- 1005: 更新失败
