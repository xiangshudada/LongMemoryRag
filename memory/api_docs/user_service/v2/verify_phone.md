服务:user-service
版本:v2
路径:POST /api/v2/user/{userId}/verify-phone
描述:验证手机号
请求参数:
- userId: integer, 必填, 用户ID
- phone: string, 必填, 手机号
- smsCode: string, 必填, 短信验证码

请求体:
```json
{
  "userId": 123,
  "phone": "13900139000",
  "smsCode": "654321"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "phone": "13900139000",
    "verified": true,
    "verifiedAt": "2024-01-15T10:30:00Z"
  }
}
```

错误码:
- 1003: 用户不存在
- 1011: 验证码错误
- 1030: 验证码已过期
- 1031: 手机号已绑定
