from flask import Blueprint

bp = Blueprint("blueprint_order", __name__, url_prefix="/order")


def create_order():
    ...


def get_orders():
    ...


def update_orders():
    ...


def delete_orders():
    ...


bp.post("")(create_order)
bp.get("")(get_orders)
bp.patch("")(update_orders)
bp.delete("")(delete_orders)
