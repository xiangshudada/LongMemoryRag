服务:system-service
版本:v1
路径:GET /api/system/backup/list
描述:获取备份列表(管理员)
请求参数:
- page: integer, 必填, 页码
- pageSize: integer, 必填, 每页数量

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"total": 10, "items": [{"backupId": "BK001", "type": "all", "status": "completed", "createdAt": "2024-01-01T00:00:00Z"}]}}
```

错误码:
- 6002: 权限不足
