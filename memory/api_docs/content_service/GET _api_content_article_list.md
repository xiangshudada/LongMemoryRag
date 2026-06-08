服务:content-service
版本:v1
路径:GET /api/content/article/list
描述:获取文章列表
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
{"code": 0, "msg": "success", "data": {"total": 200, "items": [{"articleId": 1001, "title": "测试文章", "views": 1000}]}}
```

错误码:
- 5001: 参数错误
