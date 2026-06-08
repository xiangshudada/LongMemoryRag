服务:content-service
版本:v1
路径:DELETE /api/content/comment/{commentId}
描述:删除评论
请求参数:
- commentId: integer, 必填, 评论ID

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": null}
```

错误码:
- 5006: 评论不存在
- 5004: 无权限删除
