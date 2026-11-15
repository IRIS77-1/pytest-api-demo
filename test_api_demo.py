import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class HttpUtil:
    def __init__(self, headers):
        self.headers = headers

    def post(self, url, json_data):
        return requests.post(url, headers=self.headers, json=json_data, timeout=5)

    def get(self, url):
        return requests.get(url, headers=self.headers, timeout=5)

    def put(self, url, json_data):
        return requests.put(url, headers=self.headers, json=json_data, timeout=5)

    def delete(self, url):
        return requests.delete(url, headers=self.headers, timeout=5)


@pytest.fixture(scope="module")
def get_http_client():
    """模拟登录，返回带请求头的http工具对象"""
    token = "mock-token-demo-001"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    client = HttpUtil(headers)
    yield client


@pytest.fixture(scope="module")
def new_item_id():
    """使用接口真实存在的帖子id=1"""
    return 1

def test_add_item(get_http_client):
    """新增帖子"""
    client = get_http_client
    body = {"title": "测试新增标题", "body": "测试内容", "userId": 1}
    resp = client.post(f"{BASE_URL}/posts", json_data=body)
    assert resp.status_code == 201
    res_json = resp.json()
    assert res_json["title"] == "测试新增标题"


def test_query_item(get_http_client, new_item_id):
    """查询帖子"""
    client = get_http_client
    resp = client.get(f"{BASE_URL}/posts/{new_item_id}")
    assert resp.status_code == 200
    res_json = resp.json()
    assert res_json["id"] == new_item_id


def test_update_item(get_http_client, new_item_id):
    """修改帖子"""
    client = get_http_client
    body = {"title": "标题已经被修改"}
    resp = client.put(f"{BASE_URL}/posts/{new_item_id}", json_data=body)
    assert resp.status_code == 200


def test_delete_item(get_http_client, new_item_id):
    """删除帖子"""
    client = get_http_client
    resp = client.delete(f"{BASE_URL}/posts/{new_item_id}")
    assert resp.status_code == 200


@pytest.mark.parametrize("title, expect_code", [
    ("参数用例1", 201),
    ("参数用例2", 201),

])
def test_add_param(get_http_client, title, expect_code):
    """参数化新增用例"""
    client = get_http_client
    body = {"title": title, "body": "参数化内容", "userId": 1}
    resp = client.post(f"{BASE_URL}/posts", json_data=body)
    assert resp.status_code == expect_code


def test_query_not_exist(get_http_client):
    """查询不存在的数据，预期404"""
    client = get_http_client
    resp = client.get(f"{BASE_URL}/posts/99999")
    assert resp.status_code == 404
