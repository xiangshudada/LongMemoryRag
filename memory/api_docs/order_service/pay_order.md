服务:order-service
版本:v1
路径:PUT /api/order/{orderId}/pay
描述:支付订单
请求参数:
- orderId: string, 必填, 订单号
- payMethod: string, 必填, 支付方式(alipay/wechat/card)

请求体:
```json
{
  "payMethod": "alipay"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "orderId": "ORD20240101001",
    "status": "paid",
    "payUrl": "https://pay.alipay.com/xxx"
  }
}
```

错误码:
- 2004: 订单不存在
- 2008: 订单已支付
- 2006: 订单状态不允许支付
