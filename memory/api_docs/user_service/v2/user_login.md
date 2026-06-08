服务:user-service
版本:v2
路径:POST /api/v2/user/login
描述:用户登录(支持多种方式)
请求参数:
- loginType: string, 必填, 登录方式(email/phone/username)
- account: string, 必填, 账号
- password: string, 必填, 密码
- rememberMe: boolean, 可选, 记住登录

请求体:
```json
{
  "loginType": "email",
  "account": "user@example.com",
  "password": "securePass123",
  "rememberMe": true
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
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresIn": 86400,
    "refreshExpiresIn": 2592000
  }
}
```

错误码:
- 1007: 账号或密码错误
- 1008: 账户已禁用
- 1022: 登录方式不支持
