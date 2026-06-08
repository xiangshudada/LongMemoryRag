服务:user-service
版本:v2
路径:PUT /api/v2/user/{userId}/profile
描述:更新用户资料(支持部分更新)
请求参数:
- userId: integer, 必填, 用户ID

请求体:
```json
{
  "bio": "新的个人简介",
  "gender": "male",
  "birthday": "1990-01-01",
  "nickname": "新昵称"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "userId": 123,
    "updatedAt": "2024-01-15T10:30:00Z"
  }
}
```

错误码:
- 1003: 用户不存在
- 1002: 参数错误
- 1025: 昵称已存在
