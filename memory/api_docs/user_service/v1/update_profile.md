服务:user-service
版本:v1
路径:PUT /api/user/{userId}/profile
描述:更新用户资料
请求参数:
- userId: integer, 必填, 用户ID
- bio: string, 可选, 个人简介
- gender: string, 可选, 性别(male/female/unknown)
- birthday: string, 可选, 生日(YYYY-MM-DD)

请求体:
```json
{
  "bio": "新的个人简介",
  "gender": "male",
  "birthday": "1990-01-01"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": { "userId": 123 }
}
```

错误码:
- 1003: 用户不存在
- 1002: 参数错误
