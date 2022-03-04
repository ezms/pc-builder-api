from flask import Blueprint

bp = Blueprint("blueprint_user", __name__, url_prefix="/user")


def create_user():
    ...


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


bp.post("")(create_user)
bp.get("")(get_user)
bp.patch("")(update_user)
bp.delete("")(delete_user)
bp.post("/login")(login)
bp.post("/register")(register)
