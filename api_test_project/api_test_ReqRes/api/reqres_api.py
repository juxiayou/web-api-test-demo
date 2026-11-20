import requests

class ReqResAPI:
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session  # 传入公共会话，自动带token

    # 1. 登录接口，成功返回token
    def login(self, email, password):
        url = f"{self.base_url}/login"
        body = {
            "email": email,
            "password": password
        }
        response = self.session.post(url, json=body)
        # 登录成功就返回token，失败就抛出异常
        if response.status_code == 200:
            return response.json()["token"]
        else:
            raise Exception(f"登录失败：{response.json()}")

    # 2. 查询用户列表,分页
    def get_user_list(self, page=1):
        url = f"{self.base_url}/users"
        params = {"page": page}
        response = self.session.get(url, params=params)
        return response

    # 3. 创建用户
    def create_user(self, name, job):
        url = f"{self.base_url}/users"
        body = {
            "name": name,
            "job": job
        }
        response = self.session.post(url, json=body)
        return response

    # 4. 更新用户
    def update_user(self, user_id, name, job):
        url = f"{self.base_url}/users/{user_id}"
        body = {
            "name": name,
            "job": job
        }
        response = self.session.put(url, json=body)
        return response

    # 5. 删除用户
    def delete_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        response = self.session.delete(url)
        return response
