服务:notification-service
版本:v1
路径:GET /api/notify/unread-count
描述:获取未读通知数量
请求参数:
- userId: integer, 必填, 用户ID

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"userId": 123, "unreadCount": 5}}
```

错误码:
- 5002: 用户不存在
