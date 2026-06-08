服务:payment-service
版本:v2
路径:POST /api/payment/create
描述:创建支付
请求参数:
- orderId: string, 必填, 订单号
- amount: number, 必填, 支付金额
- payMethod: string, 必填, 支付方式

请求体:
```json
{"orderId": "ORD001", "amount": 99.99, "payMethod": "alipay"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"payId": "PAY001", "payUrl": "https://pay.alipay.com/xxx"}}
```

错误码:
- 3001: 订单不存在
- 3002: 金额不匹配
- 3003: 支付方式不支持
