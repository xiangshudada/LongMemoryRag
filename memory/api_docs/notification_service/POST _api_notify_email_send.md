服务:notification-service
版本:v1
路径:POST /api/notify/email/send
描述:发送邮件
请求参数:
- email: string, 必填, 邮箱地址
- subject: string, 必填, 邮件主题
- content: string, 必填, 邮件内容

请求体:
```json
{"email": "test@example.com", "subject": "测试邮件", "content": "这是一封测试邮件"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"messageId": "MSG002"}}
```

错误码:
- 7004: 邮箱格式错误
- 7005: 发送失败
