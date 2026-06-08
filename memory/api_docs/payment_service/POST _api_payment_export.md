服务:payment-service
版本:v2
路径:POST /api/payment/export
描述:导出支付记录(管理员)
请求参数:
- startDate: string, 必填, 开始日期
- endDate: string, 必填, 结束日期
- format: string, 必填, 导出格式(csv/excel)

请求体:
```json
{
  "startDate": "2024-01-01",
  "endDate": "2024-01-31",
  "format": "excel"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "exportId": "EXP001",
    "downloadUrl": "https://cdn.example.com/exports/payment_202401.xlsx"
  }
}
```

错误码:
- 3015: 权限不足
- 3018: 数据量过大
