服务:content-service
版本:v1
路径:DELETE /api/content/article/{articleId}
描述:删除文章
请求参数:
- articleId: integer, 必填, 文章ID

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": null}
```

错误码:
- 5003: 文章不存在
- 5004: 无权限删除
