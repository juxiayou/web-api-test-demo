# ReqRes项目

官网：[https://reqres.in/](https://reqres.in/)

1. 公开、不用搭本地服务、不需要装数据库，在线直接调用；
2. 选取的测试功能对象：**登录->获取 token -> 带 token 增、查、改、删**，企业最常见业务链路；
3. 接口文档清晰，接口不多、难度适中，不是玩具接口；
4. 支持 POST / GET / PUT / DELETE，正好覆盖 CRUD。

> 
> 接口文档地址：[https://reqres.in/api-docs/](https://reqres.in/api-docs/)


## 本次要用到的 5 个核心接口

1. 登录接口：获取鉴权 Token
2. 查询用户列表：带 / 不带分页参数查询
3. 创建用户：POST 提交数据
4. 更新用户：PUT 修改已有数据
5. 删除用户：DELETE 删除指定用户

## 从 API 手册提取接口关键信息

| 接口功能 | 请求方法 | 接口地址 | 请求头 | 请求体 | 预期状态码 | 核心校验点 |
| --- | --- | --- | --- | --- | --- | --- |
| 登录 | POST | `/api/login` | Content-Type: application/json | `{"email": "eve.holt@reqres.in", "password": "cityslicka"}` | 200 | 返回包含`token`字段 |
| 查询用户列表 | GET | `/api/users?page=2` | 无 | 无 | 200 | 返回`data`数组，包含用户信息 |
| 创建用户 | POST | `/api/users` | Content-Type: application/json | `{"name": "morpheus", "job": "leader"}` | 201 | 返回 name、job 和提交一致，有 id、创建时间 |
| 更新用户 | PUT | `/api/users/2` | Content-Type: application/json | `{"name": "morpheus", "job": "zion resident"}` | 200 | 返回 name、job 和提交一致，有更新时间 |
| 删除用户 | DELETE | `/api/users/2` | 无 | 无 | 204 | 无响应体，状态码 204 表示删除成功 |