服务:notification-service
版本:v1
路径:GET /api/notify/statistics
描述:通知统计(管理员)
请求参数:
- startDate: string, 必填, 开始日期
- endDate: string, 必填, 结束日期

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"smsCount": 1000, "emailCount": 500, "pushCount": 2000, "successRate": 98.5}}
```

错误码:
- 6002: 权限不足
