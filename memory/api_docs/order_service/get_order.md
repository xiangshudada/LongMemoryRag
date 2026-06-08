服务:order-service
版本:v1
路径:GET /api/order/{orderId}
描述:获取订单详情
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
    "userId": 123,
    "productId": 456,
    "productName": "测试商品",
    "quantity": 2,
    "amount": 199.98,
    "status": "pending",
    "address": {
      "name": "张三",
      "phone": "13800138000",
      "detail": "北京市朝阳区xxx"
    },
    "createdAt": "2024-01-01T00:00:00Z"
  }
}
```

错误码:
- 2004: 订单不存在
- 2005: 无权访问
