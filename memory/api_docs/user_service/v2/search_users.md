服务:user-service
版本:v2
路径:GET /api/v2/user/search
描述:搜索用户(支持高级筛选)
请求参数:
- keyword: string, 可选, 搜索关键词
- gender: string, 可选, 性别筛选
- ageMin: integer, 可选, 最小年龄
- ageMax: integer, 可选, 最大年龄
- page: integer, 必填, 页码
- pageSize: integer, 必填, 每页数量
- sortBy: string, 可选, 排序字段(followers/posts/createdAt)

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
        "avatar": "url",
        "bio": "简介",
        "followers": 500,
        "posts": 50
      }
    ]
  }
}
```

错误码:
- 1002: 参数错误
- 1029: 排序字段无效
