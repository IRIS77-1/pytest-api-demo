# pytest-api-demo
基于 Pytest + Requests 的接口自动化测试 Demo

## 技术栈
- pytest：测试框架，fixture 前置后置、参数化
- requests：HTTP 请求库
- Allure：测试报告（可选）

## 项目说明
基于公开模拟接口 jsonplaceholder.typicode.com 完成帖子(posts)接口测试，覆盖场景：
- 新增帖子（正向、参数化多组用例）
- 查询帖子（正常查询、查询不存在数据404异常场景）
- 修改帖子
- 删除帖子

> 项目亮点：使用 fixture 封装 HTTP 请求客户端，通过 pytest.mark.parametrize 实现参数化，覆盖正向、异常多种接口测试场景，适合接口自动化入门演示。

## 项目结构
├── test_api_demo.py    # 测试用例代码

├── requirements.txt    # 依赖包清单

├── .gitignore

└── README.md


## 环境部署 & 运行
1. 安装依赖
pip install -r requirements.txt
2. 执行测试
pytest test_api_demo.py -v
3. 生成 Allure 测试报告
# 执行用例并保存结果
pytest test_api_demo.py -v --alluredir=allure-results
# 打开报告
allure serve allure-results
