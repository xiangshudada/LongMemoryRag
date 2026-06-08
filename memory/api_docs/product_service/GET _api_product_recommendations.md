服务:product-service
版本:v1
路径:GET /api/product/{productId}/recommendations
描述:获取推荐商品
请求参数:
- productId: integer, 必填, 商品ID
- limit: integer, 可选, 数量限制

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": [{"productId": 789, "name": "相关推荐商品", "price": 199.99}]}
```

错误码:
- 4003: 商品不存在
