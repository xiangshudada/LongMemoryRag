服务:notification-service
版本:v1
路径:POST /api/notify/sms/send
描述:发送短信
请求参数:
- phone: string, 必填, 手机号
- templateId: string, 必填, 模板ID
- params: object, 可选, 模板参数

请求体:
```json
{"phone": "13800138000", "templateId": "TPL001", "params": {"code": "123456"}}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"messageId": "MSG001"}}
```

错误码:
- 7001: 手机号格式错误
- 7002: 模板不存在
- 7003: 发送频率超限
