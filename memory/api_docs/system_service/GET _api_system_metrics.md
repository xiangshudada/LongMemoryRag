服务:system-service
版本:v1
路径:GET /api/system/metrics
描述:获取系统指标(管理员)
请求参数:
无

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"cpu": 45.2, "memory": 60.5, "disk": 75.0, "requestsPerSecond": 100}}
```

错误码:
- 6002: 权限不足
