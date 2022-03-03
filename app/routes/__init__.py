from flask import Blueprint, Flask
<<<<<<< HEAD
=======
from app.routes.address_routes import bp_address
>>>>>>> develop

blueprint = Blueprint("api", __name__, url_prefix="/")


def init_app(app: Flask):
    app.config["JSON_SORT_KEYS"] = False

    blueprint.register_blueprint(bp_address)
    app.register_blueprint(blueprint)
