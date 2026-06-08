服务:order-service
版本:v1
路径:GET /api/order/{orderId}/invoice
描述:获取订单发票
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
    "invoiceId": "INV20240101001",
    "type": "electronic",
    "title": "个人",
    "amount": 199.98,
    "url": "https://invoice.example.com/xxx"
  }
}
```

错误码:
- 2004: 订单不存在
- 2018: 未申请发票
