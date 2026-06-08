服务:user-service
版本:v1
路径:DELETE /api/user/{userId}
描述:删除用户
请求参数:
- userId: integer, 必填, 用户ID

请求体:
无

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": null
}
```

错误码:
- 1003: 用户不存在
- 1006: 删除失败
