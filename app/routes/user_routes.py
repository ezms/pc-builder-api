from flask import Blueprint

from app.controllers.user_controller import (confirm_email, delete_user,
                                             get_user, login, register,
                                             update_user)

bp = Blueprint("blueprint_user", __name__, url_prefix="/user")


bp.get("/confirm_email/<token>")(confirm_email)
bp.post("/register")(register)
bp.get("")(get_user)
bp.patch("")(update_user)
bp.delete("")(delete_user)
bp.post("/login")(login)
