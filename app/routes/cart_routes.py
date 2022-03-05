from flask import Blueprint
from app.controllers.cart_controller import add_product_to_cart

bp = Blueprint("blueprint_cart", __name__, url_prefix="/cart")


def get_cart():
    ...


def update_cart():
    ...


def delete_cart():
    ...


bp.post("/<int:product_id>")(add_product_to_cart)
bp.get("")(get_cart)
bp.patch("")(update_cart)
bp.delete("")(delete_cart)
