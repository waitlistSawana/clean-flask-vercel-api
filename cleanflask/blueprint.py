import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

# router for blueprint
blueprint_url = "blueprint"
bp = Blueprint(blueprint_url, __name__, url_prefix=f"/{blueprint_url}")


@bp.before_app_request
def todo_befor_app_request():
    # todo
    user_id = session.get("user_id")

    g.user = user_id

    g.whatever = "fill something you want by adding params of g"


# BaseURL/blueprint
@bp.route("/")
def blue_root():
    return "there is blueprint"


# GET BaseURL/blueprint/bluehello
@bp.route("/bluehello", methods=("GET",))
def blue_hello():
    return {
        "user_id": g.user,
        "msg": "hello, this is blueprint",
        "whatever": g.whatever,
    }


# customize function
from cleanflask.lib.text_smile import string_add_simle


# GET BaseURL/blueprint/smile
@bp.route("/smile", methods=("GET", "POST"))
def smile():

    if request.method == "GET":
        string = "i will add a smile face after your text!"
        output = string_add_simle(string)
        return output

    elif request.method == "POST":
        data = request.get_json()
        string = data["msg"]
        output = string_add_simle(string)
        return {
            "msg": output
        }
