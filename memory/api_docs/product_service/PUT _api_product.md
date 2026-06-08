服务:product-service
版本:v1
路径:PUT /api/product/{productId}
描述:更新商品信息
请求参数:
- productId: integer, 必填, 商品ID

请求体:
```json
{"name": "新商品名", "price": 199.99, "stock": 50}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"productId": 456}}
```

错误码:
- 4003: 商品不存在
- 4001: 参数错误
