from flask import Blueprint
from app.controllers import user_controller

from app.controllers.user_controller import create_user, login


from app.controllers.user_controller import get_user_orders

bp = Blueprint("blueprint_user", __name__, url_prefix="/user")


# def get_user():
#     ...


def update_user():
    ...


def delete_user():
    ...


def register():
    ...


bp.post("/register")(user_controller.create_user)
bp.get("")(user_controller.get_user)
bp.patch("")(update_user)
bp.delete("")(delete_user)
bp.post("/login")(login)
bp.post("/register")(register)
bp.get("/orders")(get_user_orders)
