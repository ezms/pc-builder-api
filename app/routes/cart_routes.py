from flask import Blueprint

from app.controllers.cart_controller import (add_product_to_cart, delete_cart,
                                             get_cart)

bp = Blueprint("blueprint_cart", __name__, url_prefix="/cart")


bp.post("/<int:product_id>")(add_product_to_cart)
bp.get("")(get_cart)
bp.delete("/<int:product_id>")(delete_cart)
