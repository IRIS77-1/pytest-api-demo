# 基于Pytest的接口自动化测试Demo
> 软件测试实习练习项目，使用pytest + requests完成RESTful接口自动化测试

## 技术栈
- Python3
- pytest：测试框架，fixture前置后置、参数化
- requests：HTTP请求库
- Allure：测试报告（可选）

## 项目说明
基于公开模拟接口 jsonplaceholder.typicode.com 完成帖子(posts)接口测试
覆盖场景：
- 新增帖子（正向、参数化多组用例）
- 查询帖子（正常查询、查询不存在数据404异常场景）
- 修改帖子
- 删除帖子

## 项目结构
├── test_api_demo.py    # 测试代码
├── requirements.txt    # 依赖包
└── README.md

## 环境部署&运行
1. 安装依赖
```bash
pip install -r requirements.txt