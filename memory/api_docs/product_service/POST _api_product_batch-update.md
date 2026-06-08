服务:product-service
版本:v1
路径:POST /api/product/batch-update
描述:批量更新商品(管理员)
请求参数:
- productIds: array, 必填, 商品ID列表
- updates: object, 必填, 更新内容

请求体:
```json
{
  "productIds": [456, 789],
  "updates": {
    "status": "off_sale",
    "price": 89.99
  }
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "successCount": 2,
    "failCount": 0
  }
}
```

错误码:
- 6002: 权限不足
- 4003: 商品不存在
