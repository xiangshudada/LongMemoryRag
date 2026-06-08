服务:payment-service
版本:v2
路径:GET /api/payment/statistics
描述:支付统计(管理员)
请求参数:
- startDate: string, 必填, 开始日期
- endDate: string, 必填, 结束日期

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"totalAmount": 99999.99, "successCount": 800, "refundAmount": 5000.00}}
```

错误码:
- 3015: 权限不足
