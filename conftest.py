import pytest
import requests
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="function")
def http_client(base_url):
    """封装http请求客户端"""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    client = {
        "session": session,
        "base_url": base_url
    }
    yield client
    session.close()
