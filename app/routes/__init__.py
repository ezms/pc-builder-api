from flask import Blueprint, Flask


blueprint = Blueprint("api", __name__, url_prefix="/")

def init_app(app: Flask):
    app.config["JSON_SORT_KEYS"] = False

    app.register_blueprint(blueprint)
