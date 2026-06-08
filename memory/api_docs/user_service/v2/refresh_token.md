服务:user-service
版本:v2
路径:POST /api/v2/user/refresh-token
描述:刷新访问令牌
请求参数:
- refreshToken: string, 必填, 刷新令牌

请求体:
```json
{
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresIn": 86400
  }
}
```

错误码:
- 1023: 刷新令牌无效
- 1024: 刷新令牌已过期
