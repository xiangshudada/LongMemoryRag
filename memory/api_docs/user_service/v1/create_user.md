服务:user-service
版本:v1
路径:POST /api/user/create
描述:创建新用户
请求参数:
- username: string, 必填, 用户名
- password: string, 必填, 密码
- phone: string, 可选, 手机号
- email: string, 可选, 邮箱

请求体:
```json
{
  "username": "string",
  "password": "string",
  "phone": "string",
  "email": "string"
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
- 1001: 用户已存在
- 1002: 参数错误
