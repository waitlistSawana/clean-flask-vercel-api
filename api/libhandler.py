import os

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

from api.lib.index_example import index_example

# router for blueprint
blueprint_url = "lib"
bp = Blueprint(blueprint_url, __name__, url_prefix=f"/{blueprint_url}")


@bp.before_app_request
def todo_befor_app_request():
    # todo
    g.whatever = "fill something you want by adding params of g."
    g.secretkey = os.environ.get("SECRET_KEY")


# BaseURL/lib
@bp.route("/")
def lib_root():
    text = "this is lib index (or other name you like)"
    msg = index_example(text)
    return {
        "msg": text,
        "msg_new": msg
    }
