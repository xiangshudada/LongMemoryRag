服务:notification-service
版本:v1
路径:GET /api/notify/list
描述:获取通知列表
请求参数:
- userId: integer, 必填, 用户ID
- page: integer, 必填, 页码
- pageSize: integer, 必填, 每页数量

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"total": 50, "items": [{"messageId": "MSG001", "title": "订单通知", "read": false, "createdAt": "2024-01-01T00:00:00Z"}]}}
```

错误码:
- 5002: 用户不存在
