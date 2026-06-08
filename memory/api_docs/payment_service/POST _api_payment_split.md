服务:payment-service
版本:v2
路径:POST /api/payment/split
描述:分账处理
请求参数:
- payId: string, 必填, 支付ID
- receivers: array, 必填, 分账接收方列表

请求体:
```json
{"payId": "PAY001", "receivers": [{"userId": 100, "amount": 30.00}, {"userId": 200, "amount": 70.00}]}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"splitId": "SP001", "status": "success"}}
```

错误码:
- 3004: 支付记录不存在
- 3013: 分账金额不匹配
- 3014: 接收方不存在
