服务:system-service
版本:v1
路径:GET /api/system/permissions
描述:获取权限列表(管理员)
请求参数:
无

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": [{"permissionId": 1, "name": "user:create", "description": "创建用户"}, {"permissionId": 2, "name": "user:delete", "description": "删除用户"}]}
```

错误码:
- 6002: 权限不足
