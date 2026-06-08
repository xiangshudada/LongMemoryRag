服务:system-service
版本:v1
路径:POST /api/system/cache/clear
描述:清空缓存(管理员)
请求参数:
- type: string, 可选, 缓存类型

请求体:
```json
{"type": "all"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"clearedCount": 100}}
```

错误码:
- 6002: 权限不足
