import pytest
import requests
from api.reqres_api import ReqResAPI

# 接口基础地址，所有接口都拼这个前缀
@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"

# 统一请求会话,不用每个请求都写requests.get
@pytest.fixture(scope="session")
def req_session():
    session = requests.Session()
    # 通用请求头
    session.headers.update({
        "Content-Type": "application/json"
    })
    
    yield session
    session.close()

# 登录后拿到的Token，鉴权的接口可复用
@pytest.fixture(scope="session")
def login_token(base_url, req_session):
    # 调用登录接口获取token
    api = ReqResAPI(base_url, req_session)
    token = api.login("eve.holt@reqres.in", "cityslicka")
    # 把token更新到会话的请求头里，后面所有请求自动带token
    req_session.headers.update({"Authorization": f"Bearer {token}"})
    return token

# 封装的API实例，用例里直接调用
@pytest.fixture(scope="session")
def reqres_api(base_url, req_session, login_token):
    return ReqResAPI(base_url, req_session)
