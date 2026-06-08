服务:order-service
版本:v1
路径:POST /api/order/{orderId}/favorite
描述:收藏订单
请求参数:
- orderId: string, 必填, 订单号
- userId: integer, 必填, 用户ID

请求体:
```json
{
  "orderId": "ORD20240101001",
  "userId": 123
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "favoriteId": 12345
  }
}
```

错误码:
- 2004: 订单不存在
- 2022: 已收藏
