服务:payment-service
版本:v2
路径:POST /api/payment/{payId}/refund
描述:支付退款
请求参数:
- payId: string, 必填, 支付ID
- amount: number, 可选, 退款金额

请求体:
```json
{"payId": "PAY001", "amount": 50.00, "reason": "用户申请退款"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"refundId": "REF001", "status": "processing"}}
```

错误码:
- 3004: 支付记录不存在
- 3006: 支付未完成
- 3007: 退款金额超限
