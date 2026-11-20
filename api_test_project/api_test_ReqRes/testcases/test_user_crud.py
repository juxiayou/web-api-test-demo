# 1. 查询用户列表（Token）
def test_get_user_list(reqres_api):
    response = reqres_api.get_user_list(page=2)
    
    # 断言：状态码200，返回的数据里有用户列表
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 2
    assert len(data["data"]) > 0  # 确认返回了用户数据
    assert "id" in data["data"][0]  # 确认每条用户数据都有id字段

# 2. 创建用户
def test_create_user(reqres_api):
    response = reqres_api.create_user(name="test_user", job="tester")
    
    # 断言：创建成功返回201，返回的名称和岗位和传入的一致
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "test_user"
    assert data["job"] == "tester"
    assert "id" in data  # 确认生成了用户ID
    assert "createdAt" in data

# 3. 更新用户
def test_update_user(reqres_api):
    response = reqres_api.update_user(user_id=2, name="update_user", job="senior_tester")
    
    # 断言：更新成功，返回的内容是修改后的
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "update_user"
    assert data["job"] == "senior_tester"
    assert "updatedAt" in data

# 4. 删除用户
def test_delete_user(reqres_api):
    response = reqres_api.delete_user(user_id=2)
    
    # 断言：删除成功返回204
    assert response.status_code == 204
