from sqlalchemy.orm import Query

from app.core.database import db
from app.models.carts_products_model import CartsProductsModel
from app.models.product_model import ProductModel


def get_all_products_query(main_table, pivot_table, pivot_table_id, main_table_id):
    products: Query = (
        db.session.query(
            ProductModel.model,
            ProductModel.price,
            ProductModel.img,
            ProductModel.description,
            ProductModel.product_id,
        )
        .select_from(ProductModel)
        .join(pivot_table)
        .join(main_table)
        .filter(pivot_table_id == main_table_id)
    )

    column_names = [column["name"] for column in products.column_descriptions]

    products = [dict(zip(column_names, prod)) for prod in products.all()]

    return products
