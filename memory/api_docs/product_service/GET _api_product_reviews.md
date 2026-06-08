服务:product-service
版本:v1
路径:GET /api/product/{productId}/reviews
描述:获取商品评价
请求参数:
- productId: integer, 必填, 商品ID
- page: integer, 必填, 页码
- pageSize: integer, 必填, 每页数量

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"total": 100, "items": [{"reviewId": 1, "rating": 5, "content": "很好"}]}}
```

错误码:
- 4003: 商品不存在
