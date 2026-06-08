服务:user-service
版本:v1
路径:POST /api/user/login
描述:用户登录
请求参数:
- username: string, 必填, 用户名或手机号
- password: string, 必填, 密码

请求体:
```json
{
  "username": "testuser",
  "password": "password123"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "userId": 123,
    "expiresIn": 86400
  }
}
```

错误码:
- 1007: 用户名或密码错误
- 1008: 账户已禁用
