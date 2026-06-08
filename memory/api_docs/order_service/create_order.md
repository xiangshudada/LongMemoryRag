服务:order-service
版本:v1
路径:POST /api/order/create
描述:创建订单
请求参数:
- userId: integer, 必填, 用户ID
- productId: integer, 必填, 商品ID
- quantity: integer, 必填, 数量
- addressId: integer, 必填, 收货地址ID

请求体:
```json
{
  "userId": 123,
  "productId": 456,
  "quantity": 2,
  "addressId": 789,
  "remark": "请尽快发货"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "orderId": "ORD20240101001",
    "amount": 199.98,
    "status": "pending"
  }
}
```

错误码:
- 2001: 商品不存在
- 2002: 库存不足
- 2003: 参数错误
