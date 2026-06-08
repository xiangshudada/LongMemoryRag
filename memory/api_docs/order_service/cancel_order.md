服务:order-service
版本:v1
路径:PUT /api/order/{orderId}/cancel
描述:取消订单
请求参数:
- orderId: string, 必填, 订单号
- reason: string, 可选, 取消原因

请求体:
```json
{
  "reason": "不想要了"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "orderId": "ORD20240101001",
    "status": "cancelled"
  }
}
```

错误码:
- 2004: 订单不存在
- 2006: 订单状态不允许取消
- 2007: 取消失败
