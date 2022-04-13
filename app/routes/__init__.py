from flask import Blueprint, Flask
from app.routes.vaccine_card_route import bp as bp_call

bp_api = Blueprint("api", __name__, url_prefix="")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_call)

    app.register_blueprint(bp_api)