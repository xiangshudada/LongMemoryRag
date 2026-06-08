服务:order-service
版本:v1
路径:POST /api/order/{orderId}/coupon
描述:订单使用优惠券
请求参数:
- orderId: string, 必填, 订单号
- couponId: string, 必填, 优惠券ID

请求体:
```json
{
  "couponId": "COUPON123"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "orderId": "ORD20240101001",
    "originalAmount": 199.98,
    "discountAmount": 20.00,
    "finalAmount": 179.98
  }
}
```

错误码:
- 2004: 订单不存在
- 2020: 优惠券无效
- 2021: 优惠券已使用
