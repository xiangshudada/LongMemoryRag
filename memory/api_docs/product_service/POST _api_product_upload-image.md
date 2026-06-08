服务:product-service
版本:v1
路径:POST /api/product/{productId}/upload-image
描述:上传商品图片
请求参数:
- productId: integer, 必填, 商品ID
- file: file, 必填, 图片文件

请求体:
```json
multipart/form-data
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"imageUrl": "https://cdn.example.com/products/456.jpg"}}
```

错误码:
- 4003: 商品不存在
- 4005: 图片格式不支持
- 4006: 图片大小超限
