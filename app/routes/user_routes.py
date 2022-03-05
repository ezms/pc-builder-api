from flask import Blueprint

from app.controllers.user_controller import register, delete_user, update_user, get_user, login


bp = Blueprint("blueprint_user", __name__, url_prefix="/user")


bp.post("/register")(register)
bp.get("")(get_user)
bp.patch("")(update_user)
bp.delete("")(delete_user)
bp.post("/login")(login)
