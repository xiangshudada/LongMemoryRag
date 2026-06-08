服务:product-service
版本:v1
路径:GET /api/product/search
描述:搜索商品
请求参数:
- keyword: string, 必填, 搜索关键词
- page: integer, 必填, 页码
- pageSize: integer, 必填, 每页数量

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"total": 50, "items": [{"productId": 456, "name": "测试商品"}]}}
```

错误码:
- 4001: 参数错误
