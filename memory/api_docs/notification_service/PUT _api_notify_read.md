服务:notification-service
版本:v1
路径:PUT /api/notify/{messageId}/read
描述:标记通知已读
请求参数:
- messageId: string, 必填, 消息ID

请求体:
```json
{"messageId": "MSG001"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": null}
```

错误码:
- 7007: 消息不存在
