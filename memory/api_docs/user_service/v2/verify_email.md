服务:user-service
版本:v2
路径:POST /api/v2/user/{userId}/verify-email
描述:验证邮箱
请求参数:
- userId: integer, 必填, 用户ID
- verifyCode: string, 必填, 验证码

请求体:
```json
{
  "userId": 123,
  "verifyCode": "123456"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "email": "user@example.com",
    "verified": true,
    "verifiedAt": "2024-01-15T10:30:00Z"
  }
}
```

错误码:
- 1003: 用户不存在
- 1020: 验证码错误
- 1030: 验证码已过期
