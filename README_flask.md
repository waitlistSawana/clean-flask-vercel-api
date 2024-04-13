# Clean Flask Api

参考自 Flask 官方的 tutorial

https://flask.palletsprojects.com/en/3.0.x/

帮助您迅速开始一个 flask api 服务器的构建，建立一个高度可用的flask后端服务器。

（不需要再从“def hello():”开始！）

项目包括：

- 创建路由和函数并引用 -- `cleanflask/__init__.py` flask 基本的 app.route 路由 

- 使用“蓝图”创建子路由 -- `cleanflask/blurprint.py` 清晰的URL结构、模块化、代码重用、拓展性、减少冲突

- 本地 sqlite 数据库 -- `cleanflask/schema.sql` 和 `cleanflask/db.py` 在官方 tutorial 查看sqlite数据库的使用技巧

## todo

- [ ] 一键部署到 Vercel

- [ ] 数据库操作集成 设置seed

## Flask

生成依赖文件: `pipenv install flask` 


## 安装项目文件

启动虚拟环境并启用：

```bash
python -m venv .venv
.venv\Scripts\activate
```


安装依赖：

方式 1  `requirements.txt`

```bash
pip install -r requirements.txt
```

方式 2  `pyproject.toml`

```bash
pip install -e .
```

方法 3  `cleanflask-1.0.0-py2.py3-none-any.whl`

```bash
pip install cleanflask-1.0.0-py2.py3-none-any.whl
```

## 启动

安装 sqlite 数据库

```bash
flask --app cleanflask init-db
```

本地运行程序

```bash
flask --app cleanflask run --debugger --reload --port 5050
```

## 测试 api

使用插件 " REST Client " ，到`debug/apitest.http`文件中进行测试。

## 覆盖率测试

请参考 flask 官方 tutorial https://flask.palletsprojects.com/en/3.0.x/tutorial/tests/

## 部署

请参阅网站托管平台的文档