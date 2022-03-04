from flask import Blueprint

from app.controllers.category_controllers import (
    create_category,
    delete_category,
    get_all_categories,
    get_category_by_id,
    update_category,
)

bp = Blueprint("blueprint_category", __name__, url_prefix="/categories")

bp.post("")(create_category)
bp.get("")(get_all_categories)
bp.get("/<int:id>")(get_category_by_id)
bp.patch("/<int:id>")(update_category)
bp.delete("/<int:id>")(delete_category)
