服务:order-service
版本:v1
路径:PUT /api/order/{orderId}/confirm
描述:确认收货
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
    "status": "completed"
  }
}
```

错误码:
- 2004: 订单不存在
- 2011: 订单未发货
- 2005: 无权访问
