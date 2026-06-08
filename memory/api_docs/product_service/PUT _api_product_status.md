服务:product-service
版本:v1
路径:PUT /api/product/{productId}/status
描述:更新商品状态
请求参数:
- productId: integer, 必填, 商品ID
- status: string, 必填, 状态(on_sale/off_sale)

请求体:
```json
{"status": "on_sale"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"productId": 456, "status": "on_sale"}}
```

错误码:
- 4003: 商品不存在
- 4008: 状态值无效
