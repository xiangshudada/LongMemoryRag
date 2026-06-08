服务:user-service
版本:v1
路径:POST /api/user/batch-create
描述:批量创建用户
请求参数:
- users: array, 必填, 用户列表

请求体:
```json
{
  "users": [
    {
      "username": "user1",
      "password": "pass1",
      "phone": "13800138001"
    },
    {
      "username": "user2",
      "password": "pass2",
      "phone": "13800138002"
    }
  ]
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "successCount": 2,
    "failCount": 0,
    "userIds": [123, 124]
  }
}
```

错误码:
- 1002: 参数错误
- 1016: 批量操作失败
