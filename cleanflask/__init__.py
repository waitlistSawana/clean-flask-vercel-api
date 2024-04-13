import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev", # 你会需要在生产环境更改它 https://flask.palletsprojects.com/en/3.0.x/tutorial/deploy/
        DATABASE=os.path.join(app.instance_path, "cleanflask.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/")
    def route():
        return "Hello, Welcome Clean Flask!"

    # connect sqlite database
    from . import db
    db.init_app(app)
    
    # register bluepirnt
    from . import blueprint
    app.register_blueprint(blueprint.bp) 

    return app
