服务:user-service
版本:v2
路径:POST /api/v2/user/follow
描述:关注用户(支持批量关注)
请求参数:
- userId: integer, 必填, 当前用户ID
- targetUserIds: array, 必填, 目标用户ID列表

请求体:
```json
{
  "userId": 123,
  "targetUserIds": [456, 789, 1000]
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "successCount": 3,
    "failCount": 0,
    "results": [
      {"userId": 456, "status": "success"},
      {"userId": 789, "status": "success"},
      {"userId": 1000, "status": "success"}
    ]
  }
}
```

错误码:
- 1003: 用户不存在
- 1018: 不能关注自己
- 1028: 部分关注失败
