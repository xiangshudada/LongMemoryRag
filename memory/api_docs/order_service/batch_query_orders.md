服务:order-service
版本:v1
路径:POST /api/order/batch-query
描述:批量查询订单
请求参数:
- orderIds: array, 必填, 订单号列表

请求体:
```json
{
  "orderIds": ["ORD20240101001", "ORD20240101002"]
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "orderId": "ORD20240101001",
      "amount": 199.98,
      "status": "pending"
    }
  ]
}
```

错误码:
- 2003: 参数错误
