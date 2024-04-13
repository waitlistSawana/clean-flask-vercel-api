import sqlite3

import click
from flask import current_app, g

# 设置和数据库有关的命令 （不用改）

def get_db():
    # g 是一个特殊的对象 如果同一个请求中第二次调用这个函数 那么会重用这个链接
    if "db" not in g:  # db 没被创建为 g 的参数 创建一个新的 g.db 连接数据库
        g.db = sqlite3.connect(
            current_app.config[
                "DATABASE"
            ],  # current_app 指向正在处理请求的 Flask 应用程序
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row  # 让开发者可以用列名来访问数据

    return g.db


def close_db(e=None):  # 用来关闭数据库链接
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()  # 连接数据库

    with current_app.open_resource("schema.sql") as f:  # 对数据库运行sql文件
        db.executescript(f.read().decode("utf8"))


@click.command("init-db")  # 现在可以用命令行调用了 init-db
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)  # 清理和释放缓存
    app.cli.add_command(init_db_command)
