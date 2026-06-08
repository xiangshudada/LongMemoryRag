服务:order-service
版本:v1
路径:POST /api/order/{orderId}/refund
描述:申请退款
请求参数:
- orderId: string, 必填, 订单号
- reason: string, 必填, 退款原因
- amount: number, 可选, 退款金额(部分退款)

请求体:
```json
{
  "reason": "商品质量问题",
  "amount": 99.99
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "refundId": "REF20240101001",
    "orderId": "ORD20240101001",
    "amount": 99.99,
    "status": "pending"
  }
}
```

错误码:
- 2004: 订单不存在
- 2012: 订单状态不允许退款
- 2013: 退款金额超限
