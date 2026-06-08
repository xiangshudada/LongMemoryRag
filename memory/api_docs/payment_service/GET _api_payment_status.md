服务:payment-service
版本:v2
路径:GET /api/payment/{withdrawId}/status
描述:查询提现状态
请求参数:
- withdrawId: string, 必填, 提现ID

请求体:
```json
无
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"withdrawId": "WD001", "status": "success", "completedAt": "2024-01-01T00:00:00Z"}}
```

错误码:
- 3011: 提现记录不存在
