服务:system-service
版本:v1
路径:POST /api/system/announcement/create
描述:创建公告(管理员)
请求参数:
- title: string, 必填, 公告标题
- content: string, 必填, 公告内容
- priority: string, 可选, 优先级(high/normal/low)

请求体:
```json
{
  "title": "系统升级公告",
  "content": "系统将于今晚22:00进行升级",
  "priority": "high"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "announcementId": 4001
  }
}
```

错误码:
- 6002: 权限不足
- 6001: 参数错误
