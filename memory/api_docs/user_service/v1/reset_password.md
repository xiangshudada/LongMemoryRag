服务:user-service
版本:v1
路径:POST /api/user/reset-password
描述:重置密码
请求参数:
- phone: string, 必填, 手机号
- smsCode: string, 必填, 短信验证码
- newPassword: string, 必填, 新密码

请求体:
```json
{
  "phone": "13800138000",
  "smsCode": "123456",
  "newPassword": "newpass123"
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
- 1011: 验证码错误
- 1012: 验证码过期
- 1002: 参数错误
