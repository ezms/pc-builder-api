from flask import Blueprint

from app.controllers import category_controllers

bp = Blueprint("blueprint_category", __name__, url_prefix="/categories")

def update_category():
    ...


def delete_category():
    ...


bp.post("")(category_controllers.create_category)
bp.get("")(category_controllers.get_all_categories)
bp.get("/<int:id>")(category_controllers.get_category_by_id)
bp.patch("/<int:id>")(update_category)
bp.delete("/<int:id>")(delete_category)
