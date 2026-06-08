服务:notification-service
版本:v1
路径:POST /api/notify/webhook/create
描述:创建Webhook通知(管理员)
请求参数:
- name: string, 必填, Webhook名称
- url: string, 必填, Webhook URL
- events: array, 必填, 触发事件列表

请求体:
```json
{
  "name": "订单通知",
  "url": "https://api.example.com/webhook/orders",
  "events": ["order.created", "order.paid"]
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "webhookId": "WH001"
  }
}
```

错误码:
- 6002: 权限不足
- 7010: URL格式错误
- 7011: Webhook名称已存在
