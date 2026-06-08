服务:system-service
版本:v1
路径:GET /api/system/logs
描述:获取系统日志(管理员)
请求参数:
- level: string, 可选, 日志级别
- startDate: string, 必填, 开始日期
- page: integer, 必填, 页码

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"total": 1000, "items": [{"level": "info", "message": "系统启动", "timestamp": "2024-01-01T00:00:00Z"}]}}
```

错误码:
- 6002: 权限不足
