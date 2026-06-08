服务:payment-service
版本:v2
路径:POST /api/payment/withdraw
描述:提现申请
请求参数:
- userId: integer, 必填, 用户ID
- amount: number, 必填, 提现金额
- accountType: string, 必填, 账户类型

请求体:
```json
{"userId": 123, "amount": 1000.00, "accountType": "bank", "accountNo": "6222021234567890"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"withdrawId": "WD001", "status": "pending"}}
```

错误码:
- 3008: 余额不足
- 3009: 账户信息错误
- 3010: 提现金额超限
