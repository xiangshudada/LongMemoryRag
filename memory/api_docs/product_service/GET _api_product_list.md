服务:product-service
版本:v1
路径:GET /api/product/list
描述:获取商品列表
请求参数:
- page: integer, 必填, 页码
- pageSize: integer, 必填, 每页数量
- categoryId: integer, 可选, 分类ID

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"total": 500, "items": [{"productId": 456, "name": "测试商品", "price": 99.99}]}}
```

错误码:
- 4001: 参数错误
