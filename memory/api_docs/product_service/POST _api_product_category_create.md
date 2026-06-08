服务:product-service
版本:v1
路径:POST /api/product/category/create
描述:创建商品分类
请求参数:
- name: string, 必填, 分类名称
- parentId: integer, 可选, 父分类ID

请求体:
```json
{"name": "新分类", "parentId": 1}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"categoryId": 3}}
```

错误码:
- 4001: 参数错误
- 4007: 父分类不存在
