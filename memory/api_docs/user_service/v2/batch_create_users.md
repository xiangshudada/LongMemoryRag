服务:user-service
版本:v2
路径:POST /api/v2/user/batch-create
描述:批量创建用户(支持导入)
请求参数:
- users: array, 必填, 用户列表
- sendWelcomeEmail: boolean, 可选, 是否发送欢迎邮件

请求体:
```json
{
  "users": [
    {
      "username": "user1",
      "password": "pass1",
      "email": "user1@example.com"
    },
    {
      "username": "user2",
      "password": "pass2",
      "email": "user2@example.com"
    }
  ],
  "sendWelcomeEmail": true
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
    "results": [
      {"userId": 123, "status": "success"},
      {"userId": 124, "status": "success"}
    ]
  }
}
```

错误码:
- 1002: 参数错误
- 1016: 批量操作失败
- 1027: 邮箱已存在
