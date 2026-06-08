服务:order-service
版本:v1
路径:GET /api/order/{orderId}/status
描述:查询订单状态
请求参数:
- orderId: string, 必填, 订单号

请求体:
无

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "orderId": "ORD20240101001",
    "status": "shipped",
    "statusText": "已发货",
    "trackingNumber": "SF1234567890"
  }
}
```

错误码:
- 2004: 订单不存在
