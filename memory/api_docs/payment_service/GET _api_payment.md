服务:payment-service
版本:v2
路径:GET /api/payment/{payId}
描述:查询支付状态
请求参数:
- payId: string, 必填, 支付ID

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"payId": "PAY001", "status": "success", "amount": 99.99, "paidAt": "2024-01-01T00:00:00Z"}}
```

错误码:
- 3004: 支付记录不存在
