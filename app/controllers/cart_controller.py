from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.carts_model import CartsModel
from app.models.user_model import UserModel
from app.models.product_model import ProductModel
from app.models.carts_products_model import CartsProductsModel
from app.core.database import db


@jwt_required()
def add_product_to_cart(product_id):

    current_user = get_jwt_identity()

    user = UserModel.query.get(current_user["user_id"])
    cart_id = user.cart.cart_id

    product = ProductModel.query.get(product_id)

    if not product:
        return {"error": f"no product found with id {product_id}"}, HTTPStatus.NOT_FOUND

    cart_product = CartsProductsModel(cart_id=cart_id, product_id=product_id)

    products = (
        db.session.query(
            ProductModel.model,
            ProductModel.price,
            ProductModel.img,
            ProductModel.description,
            ProductModel.product_id,
        )
        .select_from(ProductModel)
        .join(CartsProductsModel)
        .join(CartsModel)
        .filter(CartsProductsModel.cart_id == cart_id)
    )

    cart_total = sum([prod[1] for prod in products.all()])

    user.cart.total = cart_total

    try:
        db.session.add(cart_product)
        db.session.commit()
    except:
        db.session.close()
        raise

    return jsonify(product)
