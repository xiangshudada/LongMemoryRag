服务:system-service
版本:v1
路径:POST /api/system/backup
描述:系统备份(管理员)
请求参数:
- type: string, 必填, 备份类型(database/files/all)

请求体:
```json
{"type": "all"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"backupId": "BK001", "status": "processing"}}
```

错误码:
- 6002: 权限不足
- 6003: 备份类型无效
