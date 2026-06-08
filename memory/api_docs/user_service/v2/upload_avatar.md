服务:user-service
版本:v2
路径:POST /api/v2/user/upload-avatar
描述:上传用户头像(支持裁剪)
请求参数:
- userId: integer, 必填, 用户ID
- file: file, 必填, 图片文件
- cropX: integer, 可选, 裁剪X坐标
- cropY: integer, 可选, 裁剪Y坐标
- cropSize: integer, 可选, 裁剪尺寸

请求体:
multipart/form-data

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "avatarUrl": "https://cdn.example.com/avatars/123.jpg",
    "thumbnailUrl": "https://cdn.example.com/avatars/123_thumb.jpg",
    "width": 800,
    "height": 800
  }
}
```

错误码:
- 1003: 用户不存在
- 1014: 文件格式不支持
- 1015: 文件大小超限
- 1026: 图片尺寸过小
