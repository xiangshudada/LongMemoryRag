服务:system-service
版本:v1
路径:POST /api/system/maintenance
描述:设置维护模式(管理员)
请求参数:
- enabled: boolean, 必填, 是否启用
- reason: string, 可选, 维护原因

请求体:
```json
{"enabled": true, "reason": "系统升级"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": null}
```

错误码:
- 6002: 权限不足
