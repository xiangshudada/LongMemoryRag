服务:product-service
版本:v1
路径:POST /api/product/create
描述:创建商品
请求参数:
- name: string, 必填, 商品名称
- price: number, 必填, 价格
- stock: integer, 必填, 库存

请求体:
```json
{"name": "测试商品", "price": 99.99, "stock": 100, "category": "electronics"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"productId": 456}}
```

错误码:
- 4001: 参数错误
- 4002: 分类不存在
