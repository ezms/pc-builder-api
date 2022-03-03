from flask import Blueprint

bp = Blueprint("blueprint_cart", __name__, url_prefix="/cart")


def create_cart():
    ...


def get_cart():
    ...


def update_cart():
    ...


def delete_cart():
    ...


bp.post("")(create_cart)
bp.get("")(get_cart)
bp.patch("")(update_cart)
bp.delete("")(delete_cart)
