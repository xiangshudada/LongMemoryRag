服务:user-service
版本:v2
路径:GET /api/v2/user/{userId}/activities
描述:获取用户活动记录
请求参数:
- userId: integer, 必填, 用户ID
- type: string, 可选, 活动类型筛选(login/post/like/follow)
- startDate: string, 可选, 开始日期
- endDate: string, 可选, 结束日期
- page: integer, 必填, 页码
- pageSize: integer, 必填, 每页数量

请求体:
无

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "total": 500,
    "page": 1,
    "pageSize": 20,
    "items": [
      {
        "activityId": 1,
        "type": "login",
        "description": "用户登录",
        "ip": "192.168.1.1",
        "device": "Chrome/Windows",
        "createdAt": "2024-01-15T10:30:00Z"
      }
    ]
  }
}
```

错误码:
- 1003: 用户不存在
- 1032: 活动类型无效
