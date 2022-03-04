from flask import Blueprint

from app.controllers import product_controllers

bp = Blueprint("products", __name__, url_prefix="/products")


def get_products():
    ...


def get_product_by_id():
    ...


def update_product():
    ...


def delete_product():
    ...


bp.post("")(product_controllers.create_product)
bp.get("")(get_products)
bp.get("<int:product_id>")(get_product_by_id)
bp.patch("<int:product_id>")(update_product)
bp.delete("<int:product_id>")(delete_product)
