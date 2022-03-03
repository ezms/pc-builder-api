from flask import Blueprint, Flask

from app.routes.order_routes import bp as bp_order

blueprint = Blueprint("api", __name__, url_prefix="/")

def init_app(app: Flask):
    app.config["JSON_SORT_KEYS"] = False

    
    blueprint.register_blueprint(bp_order)
    app.register_blueprint(blueprint)
