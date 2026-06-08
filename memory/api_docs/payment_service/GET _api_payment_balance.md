服务:payment-service
版本:v2
路径:GET /api/payment/balance
描述:查询账户余额
请求参数:
- userId: integer, 必填, 用户ID

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"userId": 123, "balance": 1234.56, "currency": "CNY"}}
```

错误码:
- 3012: 用户不存在
