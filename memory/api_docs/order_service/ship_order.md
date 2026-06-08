服务:order-service
版本:v1
路径:PUT /api/order/{orderId}/ship
描述:发货(管理员)
请求参数:
- orderId: string, 必填, 订单号
- trackingNumber: string, 必填, 物流单号
- carrier: string, 必填, 物流公司

请求体:
```json
{
  "trackingNumber": "SF1234567890",
  "carrier": "顺丰速运"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "orderId": "ORD20240101001",
    "status": "shipped"
  }
}
```

错误码:
- 2004: 订单不存在
- 2009: 订单未支付
- 2010: 权限不足
