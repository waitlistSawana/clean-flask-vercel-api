from flask import Flask, request

app = Flask(__name__)

# 官方的示例 所有的东西都在./下完成

@app.route('/')
def home():
    return 'Hello, World!'


@app.route("/get", methods=['GET'])
def get():
    return "welcome, you could get someting'"


@app.route("/post", methods=['POST'])
def post():
    data = request.get_json()
    if data is None:
        return "fail to get data"
    else:
        return {
            "whatyoupost": data
        }    


@app.route("/double", methods=("GET", "POST"))
def double():
    
    if request.method == "GET":
        return {
            "getmsg": "you could even deal with them together'"
        }
    
    elif request.method == "POST":
        data = request.get_json()
        return {
            "postmsg": data
        }


# register bluepirnt
from . import blueprint
if 'bp' not in app.blueprints:
    app.register_blueprint(blueprint.bp)
else:
    print('Blueprint already exists, skipping registration.')


if __name__ == '__main__':
    app.run(debug=True)