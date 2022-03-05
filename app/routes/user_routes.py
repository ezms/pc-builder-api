from flask import Blueprint
from app.controllers.user_controller import create_user, update_user, get_user, login


bp = Blueprint("blueprint_user", __name__, url_prefix="/user")


def delete_user():
    ...


def register():
    ...


bp.post("/register")(create_user)
bp.get("")(get_user)
bp.patch("")(update_user)
bp.delete("")(delete_user)
bp.post("/login")(login)
