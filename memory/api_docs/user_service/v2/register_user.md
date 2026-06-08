服务:user-service
版本:v2
路径:POST /api/v2/user/register
描述:用户注册(支持邮箱验证码)
请求参数:
- username: string, 必填, 用户名
- password: string, 必填, 密码
- email: string, 必填, 邮箱
- verifyCode: string, 必填, 邮箱验证码
- inviteCode: string, 可选, 邀请码

请求体:
```json
{
  "username": "newuser",
  "password": "securePass123",
  "email": "user@example.com",
  "verifyCode": "123456",
  "inviteCode": "INV001"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "userId": 123,
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresIn": 86400
  }
}
```

错误码:
- 1001: 用户已存在
- 1002: 参数错误
- 1020: 邮箱验证码错误
- 1021: 邀请码无效
