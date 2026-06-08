服务:system-service
版本:v1
路径:POST /api/system/user/assign-role
描述:分配用户角色(管理员)
请求参数:
- userId: integer, 必填, 用户ID
- roleId: integer, 必填, 角色ID

请求体:
```json
{"userId": 123, "roleId": 10}
```

响应体:
```json
{"code": 0, "msg": "success", "data": null}
```

错误码:
- 6002: 权限不足
- 5002: 用户不存在
- 6005: 角色不存在
