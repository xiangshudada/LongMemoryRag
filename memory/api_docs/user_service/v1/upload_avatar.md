服务:user-service
版本:v1
路径:POST /api/user/upload-avatar
描述:上传用户头像
请求参数:
- userId: integer, 必填, 用户ID
- file: file, 必填, 图片文件

请求体:
multipart/form-data

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "avatarUrl": "https://cdn.example.com/avatars/123.jpg"
  }
}
```

错误码:
- 1003: 用户不存在
- 1014: 文件格式不支持
- 1015: 文件大小超限
