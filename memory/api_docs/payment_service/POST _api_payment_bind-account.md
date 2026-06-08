服务:payment-service
版本:v2
路径:POST /api/payment/bind-account
描述:绑定收款账户
请求参数:
- userId: integer, 必填, 用户ID
- accountType: string, 必填, 账户类型
- accountNo: string, 必填, 账号

请求体:
```json
{"userId": 123, "accountType": "alipay", "accountNo": "alipay@example.com"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"accountId": "ACC001"}}
```

错误码:
- 3012: 用户不存在
- 3016: 账号格式错误
