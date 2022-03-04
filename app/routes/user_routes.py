from flask import Blueprint

from app.controllers.user_controller import create_user


bp = Blueprint("blueprint_user", __name__, url_prefix="/user")


def get_user():
    ...


def update_user():
    ...


def delete_user():
    ...


def login():
    ...


def register():
    ...


bp.post("/register")(create_user)
bp.get("")(get_user)
bp.patch("")(update_user)
bp.delete("")(delete_user)
bp.post("/login")(login)
bp.post("/register")(register)
