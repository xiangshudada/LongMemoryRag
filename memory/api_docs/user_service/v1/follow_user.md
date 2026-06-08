服务:user-service
版本:v1
路径:POST /api/user/follow
描述:关注用户
请求参数:
- userId: integer, 必填, 当前用户ID
- targetUserId: integer, 必填, 目标用户ID

请求体:
```json
{
  "userId": 123,
  "targetUserId": 456
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "followId": 789
  }
}
```

错误码:
- 1003: 用户不存在
- 1018: 不能关注自己
- 1019: 已关注
