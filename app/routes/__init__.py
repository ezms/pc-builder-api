from flask import Blueprint, Flask, render_template

from app.routes.address_routes import bp_address
from app.routes.cart_routes import bp as bp_cart
from app.routes.category_routes import bp as bp_category
from app.routes.order_routes import bp as bp_orders
from app.routes.product_routes import bp as bp_product
from app.routes.user_routes import bp as bp_user

blueprint = Blueprint("api", __name__, url_prefix="/")


def init_app(app: Flask):
    app.config["JSON_SORT_KEYS"] = False

    @blueprint.get("")
    def home():
        return render_template("base.html")

    blueprint.register_blueprint(bp_orders)
    blueprint.register_blueprint(bp_address)
    blueprint.register_blueprint(bp_cart)
    blueprint.register_blueprint(bp_user)
    blueprint.register_blueprint(bp_product)
    blueprint.register_blueprint(bp_category)

    app.register_blueprint(blueprint)
