服务:order-service
版本:v1
路径:GET /api/order/list
描述:获取订单列表(分页)
请求参数:
- userId: integer, 必填, 用户ID
- page: integer, 必填, 页码
- pageSize: integer, 必填, 每页数量
- status: string, 可选, 订单状态筛选

请求体:
无

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "total": 50,
    "page": 1,
    "pageSize": 20,
    "items": [
      {
        "orderId": "ORD20240101001",
        "amount": 199.98,
        "status": "pending",
        "createdAt": "2024-01-01T00:00:00Z"
      }
    ]
  }
}
```

错误码:
- 2003: 参数错误
