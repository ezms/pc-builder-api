from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Query
from werkzeug.exceptions import NotFound

from app.core.database import db
from app.models.carts_model import CartsModel
from app.models.carts_products_model import CartsProductsModel
from app.models.product_model import ProductModel
from app.models.user_model import UserModel


@jwt_required()
def add_product_to_cart(product_id):

    current_user = get_jwt_identity()

    user = UserModel.query.get(current_user["user_id"])
    cart_id = user.cart.cart_id

    product = ProductModel.query.get(product_id)

    if not product:
        return {"error": f"no product found with id {product_id}"}, HTTPStatus.NOT_FOUND

    cart_product = CartsProductsModel(cart_id=cart_id, product_id=product_id)

    cart_total = user.cart.total + product.price

    user.cart.total = cart_total

    try:
        db.session.add(cart_product)
        db.session.commit()
    except:
        db.session.close()
        raise

    return jsonify(product)


@jwt_required()
def delete_cart(product_id):
    try:
        user_id = get_jwt_identity()["user_id"]

        cart: Query = CartsModel.query.filter_by(user_id=user_id).first_or_404(
            description="Cart not found!"
        )

        product_cart = CartsProductsModel.query.filter_by(
            product_id=product_id, cart_id=cart.cart_id
        ).first_or_404(description="Product not found!")

        product = ProductModel.query.filter_by(product_id=product_id).first_or_404(
            description="Product not found!"
        )

        cart.total = cart.total - product.price if cart.total - product.price > 0 else 0

        db.session.delete(product_cart)
        db.session.commit()

        return {"msg": "Cart has been delete!"}, HTTPStatus.OK
    except NotFound as err:
        return {"err": err.description}, HTTPStatus.NOT_FOUND
