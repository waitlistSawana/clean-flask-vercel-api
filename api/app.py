from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/get", methods=["GET"])
def get():
    return "welcome, you could get someting'"


@app.route("/post", methods=["POST"])
def post():
    data = request.get_json()
    return {"whatyoupost": data}


@app.route("/double", methods=("GET", "POST"))
def double():

    if request.method == "GET":
        return {"getmsg": "you could even deal with them together'"}

    elif request.method == "POST":
        data = request.get_json()
        return {"postmsg": data}


# register bluepirnt
from blueprint import blueprint
app.register_blueprint(blueprint.bp)

from blueprint import libhandler
app.register_blueprint(libhandler.bp)

# 锁定输出格式为 utf-8
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

if __name__ == "__main__":
    app.run(debug=False)
