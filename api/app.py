from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route("/get", methods=['GET'])
def get():
    return "welcome, you could get someting'"


@app.route("/post", methods=['POST'])
def post():
    data = request.get_json()
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
app.register_blueprint(blueprint.bp)


if __name__ == '__main__':
    app.run(debug=False)