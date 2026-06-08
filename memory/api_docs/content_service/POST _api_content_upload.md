服务:content-service
版本:v1
路径:POST /api/content/upload
描述:上传文件
请求参数:
- file: file, 必填, 文件
- type: string, 必填, 文件类型(image/video/document)

请求体:
```json
multipart/form-data
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"fileUrl": "https://cdn.example.com/files/xxx.pdf"}}
```

错误码:
- 5008: 文件类型不支持
- 5009: 文件大小超限
