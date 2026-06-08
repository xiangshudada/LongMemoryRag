服务:user-service
版本:v1
路径:POST /api/user/logout
描述:用户登出
请求参数:
- token: string, 必填, 登录令牌

请求体:
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": null
}
```

错误码:
- 1009: 令牌无效
- 1010: 令牌已过期
