服务:notification-service
版本:v1
路径:POST /api/notify/batch-send
描述:批量发送通知
请求参数:
- userIds: array, 必填, 用户ID列表
- title: string, 必填, 通知标题
- content: string, 必填, 通知内容

请求体:
```json
{"userIds": [123, 456, 789], "title": "系统通知", "content": "系统升级通知"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"successCount": 3, "failCount": 0}}
```

错误码:
- 7008: 参数错误
