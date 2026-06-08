服务:order-service
版本:v1
路径:PUT /api/order/{orderId}/address
描述:修改收货地址
请求参数:
- orderId: string, 必填, 订单号
- addressId: integer, 必填, 新地址ID

请求体:
```json
{
  "addressId": 790
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "orderId": "ORD20240101001"
  }
}
```

错误码:
- 2004: 订单不存在
- 2016: 订单已发货不可修改
- 2017: 地址不存在
