from flask import Blueprint

from app.controllers.order_controller import get_order_by_id, get_orders

bp = Blueprint("blueprint_order", __name__, url_prefix="/order")


def create_order():
    ...


def update_orders():
    ...


def delete_orders():
    ...


bp.post("")(create_order)
bp.get("")(get_orders)
bp.get("/<int:order_id>")(get_order_by_id)
bp.patch("")(update_orders)
bp.delete("")(delete_orders)
