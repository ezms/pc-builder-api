from flask import Blueprint

bp = Blueprint("blueprint_category", __name__, url_prefix="/categories")


def create_category():
    ...


def get_categories():
    ...


def get_category_by_id():
    ...


def update_category():
    ...


def delete_category():
    ...


bp.post("")(create_category)
bp.get("")(get_categories)
bp.get("/<int:category_id>")(get_category_by_id)
bp.patch("/<int:category_id>")(update_category)
bp.delete("/<int:category_id>")(delete_category)
