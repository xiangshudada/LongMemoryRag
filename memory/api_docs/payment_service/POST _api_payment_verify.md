服务:payment-service
版本:v2
路径:POST /api/payment/verify
描述:支付验证
请求参数:
- payId: string, 必填, 支付ID
- verifyCode: string, 必填, 验证码

请求体:
```json
{"payId": "PAY001", "verifyCode": "123456"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"verified": true}}
```

错误码:
- 3004: 支付记录不存在
- 3017: 验证码错误
