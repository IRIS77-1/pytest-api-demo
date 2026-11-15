import pytest
import yaml
import requests
import logging

logger = logging.getLogger(__name__)

# 读取yaml数据
def load_yaml(filepath):
    with open(filepath, encoding="utf-8") as f:
        return yaml.safe_load(f)

test_data = load_yaml("test_data.yaml")

# 查询帖子用例
@pytest.mark.parametrize("case", test_data["get_post"])
def test_get_post(http_client, case):
    url = f'{http_client["base_url"]}/posts/{case["post_id"]}'
    try:
        resp = http_client["session"].get(url)
        logger.info(f"【{case['case_name']}】 请求地址：{url}，响应码：{resp.status_code}")
        assert resp.status_code == case["expect_status"], f"预期{case['expect_status']}，实际{resp.status_code}"
    except Exception as e:
        logger.error(f"用例异常：{e}")
        raise

# 新增帖子用例
@pytest.mark.parametrize("case", test_data["create_post"])
def test_create_post(http_client, case):
    url = f'{http_client["base_url"]}/posts'
    payload = case["payload"]
    try:
        resp = http_client["session"].post(url, json=payload)
        logger.info(f"【{case['case_name']}】 请求地址：{url}，响应码：{resp.status_code}")
        assert resp.status_code == case["expect_status"]
    except Exception as e:
        logger.error(f"用例异常：{e}")
        raise
