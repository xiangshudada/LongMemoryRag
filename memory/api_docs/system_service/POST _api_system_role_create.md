服务:system-service
版本:v1
路径:POST /api/system/role/create
描述:创建角色(管理员)
请求参数:
- name: string, 必填, 角色名称
- permissions: array, 必填, 权限ID列表

请求体:
```json
{"name": "运营人员", "permissions": [1, 2, 3]}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"roleId": 10}}
```

错误码:
- 6002: 权限不足
- 6004: 角色名已存在
