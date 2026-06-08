服务:notification-service
版本:v1
路径:POST /api/notify/template/create
描述:创建通知模板(管理员)
请求参数:
- name: string, 必填, 模板名称
- type: string, 必填, 类型(sms/email/push)
- content: string, 必填, 模板内容

请求体:
```json
{"name": "验证码模板", "type": "sms", "content": "您的验证码是{code}"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"templateId": "TPL001"}}
```

错误码:
- 6002: 权限不足
- 7009: 模板名已存在
