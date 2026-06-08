服务:content-service
版本:v1
路径:POST /api/content/article/create
描述:创建文章
请求参数:
- title: string, 必填, 文章标题
- content: string, 必填, 文章内容
- authorId: integer, 必填, 作者ID

请求体:
```json
{"title": "测试文章", "content": "文章内容...", "authorId": 123, "tags": ["技术", "编程"]}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"articleId": 1001}}
```

错误码:
- 5001: 参数错误
- 5002: 作者不存在
