服务:product-service
版本:v1
路径:PUT /api/product/{productId}/stock
描述:更新商品库存
请求参数:
- productId: integer, 必填, 商品ID
- stock: integer, 必填, 新库存数量

请求体:
```json
{"stock": 200}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"productId": 456, "stock": 200}}
```

错误码:
- 4003: 商品不存在
- 4001: 参数错误
