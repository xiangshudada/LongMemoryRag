服务:payment-service
版本:v2
路径:GET /api/payment/list
描述:获取支付列表
请求参数:
- userId: integer, 必填, 用户ID
- page: integer, 必填, 页码
- pageSize: integer, 必填, 每页数量

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"total": 100, "items": [{"payId": "PAY001", "amount": 99.99, "status": "success"}]}}
```

错误码:
- 3003: 参数错误
