from flask import Blueprint
from app.controllers import user_controller


bp = Blueprint("blueprint_user", __name__, url_prefix="/user")


def update_user():
    ...


def delete_user():
    ...


bp.post("/register")(user_controller.register)
bp.get("")(user_controller.get_user)
bp.patch("")(update_user)
bp.delete("")(delete_user)
bp.post("/login")(user_controller.login)
