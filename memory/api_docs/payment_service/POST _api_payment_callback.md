服务:payment-service
版本:v2
路径:POST /api/payment/{payId}/callback
描述:支付回调处理
请求参数:
- payId: string, 必填, 支付ID
- status: string, 必填, 支付状态

请求体:
```json
{"payId": "PAY001", "status": "success", "transactionId": "TXN123"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": null}
```

错误码:
- 3004: 支付记录不存在
- 3005: 回调签名验证失败
