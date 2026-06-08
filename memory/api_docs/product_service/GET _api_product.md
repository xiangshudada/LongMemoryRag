服务:product-service
版本:v1
路径:GET /api/product/{productId}
描述:获取商品详情
请求参数:
- productId: integer, 必填, 商品ID

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"productId": 456, "name": "测试商品", "price": 99.99, "stock": 100, "images": ["url1", "url2"]}}
```

错误码:
- 4003: 商品不存在
