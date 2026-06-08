服务:product-service
版本:v1
路径:GET /api/product/categories
描述:获取商品分类列表
请求参数:
无

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": [{"categoryId": 1, "name": "电子产品", "parentId": null}, {"categoryId": 2, "name": "手机", "parentId": 1}]}
```

错误码:
无
