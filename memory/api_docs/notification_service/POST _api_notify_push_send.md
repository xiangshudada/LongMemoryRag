服务:notification-service
版本:v1
路径:POST /api/notify/push/send
描述:推送通知
请求参数:
- userId: integer, 必填, 用户ID
- title: string, 必填, 通知标题
- content: string, 必填, 通知内容

请求体:
```json
{"userId": 123, "title": "订单通知", "content": "您的订单已发货"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"messageId": "MSG003"}}
```

错误码:
- 5002: 用户不存在
- 7006: 推送失败
