服务:user-service
版本:v1
路径:GET /api/user/list
描述:获取用户列表(分页)
请求参数:
- page: integer, 必填, 页码,默认1
- pageSize: integer, 必填, 每页数量,默认20
- keyword: string, 可选, 搜索关键词

请求体:
无

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "total": 100,
    "page": 1,
    "pageSize": 20,
    "items": [
      {
        "userId": 123,
        "username": "testuser",
        "phone": "13800138000",
        "createdAt": "2024-01-01T00:00:00Z"
      }
    ]
  }
}
```

错误码:
- 1002: 参数错误
