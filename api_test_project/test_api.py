import pytest
import requests

# 要测的两种情况
# 第一种：正常的网址，预期返回 200（成功）
# 第二种：故意写错的网址，预期返回 404（找不到网页）
test_cases = [
    ("https://v1.hitokoto.cn/", 200),        
    ("https://v1.hitokoto.cn/abc123", 404),  
]


@pytest.mark.parametrize("url, expected_code", test_cases)
def test_hitokoto(url, expected_code):
    
    response = requests.get(url)
    
    # 如果网址是对的，它应该等于 200；如果是错的，它应该等于 404
    assert response.status_code == expected_code
    
    # 当测的是正确的网址（200）时，确认拿到的内容有hitokoto字段
    if expected_code == 200:
        data = response.json()
        assert "hitokoto" in data
