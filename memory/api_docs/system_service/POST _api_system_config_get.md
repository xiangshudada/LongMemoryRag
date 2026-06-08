服务:system-service
版本:v1
路径:POST /api/system/config/get
描述:获取系统配置
请求参数:
- key: string, 必填, 配置键

请求体:
```json
{"key": "site_name"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"key": "site_name", "value": "我的网站"}}
```

错误码:
- 6001: 配置项不存在
