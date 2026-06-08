服务:content-service
版本:v1
路径:GET /api/content/search
描述:搜索内容
请求参数:
- keyword: string, 必填, 搜索关键词
- type: string, 可选, 类型(article/comment)
- page: integer, 必填, 页码

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"total": 30, "items": [{"type": "article", "id": 1001, "title": "测试文章"}]}}
```

错误码:
- 5001: 参数错误
