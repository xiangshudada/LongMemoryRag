服务:payment-service
版本:v2
路径:POST /api/payment/recharge
描述:账户充值
请求参数:
- userId: integer, 必填, 用户ID
- amount: number, 必填, 充值金额
- payMethod: string, 必填, 支付方式

请求体:
```json
{"userId": 123, "amount": 500.00, "payMethod": "wechat"}
```

响应体:
```json
{"code": 0, "msg": "success", "data": {"rechargeId": "RC001", "payUrl": "https://pay.wechat.com/xxx"}}
```

错误码:
- 3012: 用户不存在
- 3003: 参数错误
