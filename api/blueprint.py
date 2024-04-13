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

# router for blueprint
blueprint_url = "blueprint"
bp = Blueprint(blueprint_url, __name__, url_prefix=f"/{blueprint_url}")


@bp.before_app_request
def todo_befor_app_request():
    # todo
    g.whatever = "fill something you want by adding params of g."
    g.secretkey = os.environ.get("SECRET_KEY")


# BaseURL/blueprint
@bp.route("/")
def blue_root():
    return {"msg": "there is blueprint"}


# BaseURL/blueprint
@bp.route("/useg", methods=["GET"])
def use_g():
    return {"g": g.whatever, "secretkey": g.secretkey}
