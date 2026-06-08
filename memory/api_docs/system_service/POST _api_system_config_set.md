服务:system-service
版本:v1
路径:POST /api/system/config/set
描述:设置系统配置(管理员)
请求参数:
- key: string, 必填, 配置键
- value: string, 必填, 配置值

请求体:
```json
{"key": "site_name", "value": "新网站名"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": null}
```

错误码:
- 6001: 配置项不存在
- 6002: 权限不足
