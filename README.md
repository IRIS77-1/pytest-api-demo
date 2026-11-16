# pytest-api-demo
# FastAPI 文章接口自动化测试项目
基于 Pytest + Requests + Allure 实现的接口自动化测试，对 FastAPI 后端文章CRUD接口做功能测试。

##  技术栈
- Python 3.x
- pytest：测试框架
- requests：发送HTTP请求
- allure-pytest：生成可视化测试报告
- MySQL：测试数据库（fixture提供数据库游标）

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

├── test_post_db.py      # 自动化测试用例文件

├── allure-results/      # allure 原始结果目录（运行后生成）

├── allure-report/       # allure 静态报告目录（生成后生成）

└── README.md            # 项目说明

##  测试接口清单
| 接口 | 请求方法 | 测试场景 |
| ---- | -------- | -------- |
| /posts | POST | 新增文章 |
| /posts | GET | 查询文章列表 |
| /posts/{id} | GET | 查询单篇文章 |
| /posts/{id} | PUT | 修改文章 |
| /posts/{id} | DELETE | 删除文章 |


## 环境部署 & 运行
```
1. 安装依赖
```bash
pip install pytest requests allure-pytest
```

2. 安装 Allure 命令行工具（需要配置环境变量）
3. 启动后端 FastAPI 服务：`http://127.0.0.1:8000`
4. 数据库提前建好 posts 表，pytest fixture `db_cursor` 提供数据库连接

## 运行测试命令

1. 执行用例，收集 allure 结果

```
pytest test_post_db.py -v -s --alluredir=allure-results
```

2. 启动可视化报告（自动打开浏览器）

```
allure serve allure-results
```

3. 生成静态报告文件

```
allure generate allure-results -o allure-report --clean
allure open allure-report
```
##  项目特点

- 每个用例前置在数据库插入测试数据并 commit，避免事务锁导致超时
- 使用 allure feature/story 标签管理模块和测试点
- 每个用例打印返回结果，方便调试
- 适配后端真实状态码：新增返回 201
