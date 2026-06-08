服务:system-service
版本:v1
路径:POST /api/system/notify
描述:发送系统通知(管理员)
请求参数:
- title: string, 必填, 通知标题
- content: string, 必填, 通知内容
- targetUsers: array, 可选, 目标用户列表

请求体:
```json
{"title": "系统维护通知", "content": "系统将于今晚22:00进行维护", "targetUsers": [123, 456]}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"notifyId": 3001}}
```

错误码:
- 6002: 权限不足
- 6001: 参数错误
