from flask import Blueprint

bp = Blueprint("products", __name__, url_prefix="/products")


def create_product():
    ...


def get_products():
    ...


def get_product_by_id():
    ...


def update_product():
    ...


def delete_product():
    ...


bp.post("")(create_product)
bp.get("")(get_products)
bp.get("<int:product_id>")(get_product_by_id)
bp.patch("<int:product_id>")(update_product)
bp.delete("<int:product_id>")(delete_product)
