服务:order-service
版本:v1
路径:POST /api/order/{orderId}/comment
描述:评价订单
请求参数:
- orderId: string, 必填, 订单号
- rating: integer, 必填, 评分(1-5)
- content: string, 可选, 评价内容

请求体:
```json
{
  "rating": 5,
  "content": "商品很好,非常满意"
}
```

响应体:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "commentId": 12345
  }
}
```

错误码:
- 2004: 订单不存在
- 2014: 订单未完成
- 2015: 重复评价
