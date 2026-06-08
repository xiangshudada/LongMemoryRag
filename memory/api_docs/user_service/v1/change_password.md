服务:user-service
版本:v1
路径:POST /api/user/change-password
描述:修改密码
请求参数:
- userId: integer, 必填, 用户ID
- oldPassword: string, 必填, 旧密码
- newPassword: string, 必填, 新密码

请求体:
```json
{
  "oldPassword": "oldpass123",
  "newPassword": "newpass456"
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
- 1013: 旧密码错误
- 1002: 参数错误
