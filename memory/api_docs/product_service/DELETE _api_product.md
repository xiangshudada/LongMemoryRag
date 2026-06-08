服务:product-service
版本:v1
路径:DELETE /api/product/{productId}
描述:删除商品
请求参数:
- productId: integer, 必填, 商品ID

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": null}
```

错误码:
- 4003: 商品不存在
- 4004: 商品已有关联订单
