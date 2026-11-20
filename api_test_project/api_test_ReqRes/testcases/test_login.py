import pytest

# 正向]：正确账号密码，登录成功，能拿到token
def test_login_success(reqres_api):
    # 直接调用封装好的登录方法，成功会返回token
    token = reqres_api.login("eve.holt@reqres.in", "cityslicka")
    # 断言：token不是空字符串
    assert token is not None
    assert len(token) > 0

# 异常：缺少密码，登录失败，返回400
def test_login_fail_missing_password(base_url, req_session):
    url = f"{base_url}/login"
    body = {"email": "eve.holt@reqres.in"}  # 故意不传password
    response = req_session.post(url, json=body)
    
    # 断言：状态码是400，返回错误提示
    assert response.status_code == 400
    assert "Missing password" in response.json()["error"]
