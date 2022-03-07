from datetime import datetime
from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Query
from werkzeug.exceptions import NotFound

from app.core.database import db
from app.models.carts_model import CartsModel
from app.models.carts_products_model import CartsProductsModel
from app.models.order_model import OrdersModel
from app.models.order_product_model import OrdersProductsModel
from app.models.product_model import ProductModel
from app.models.user_model import UserModel
from app.services.products_query_services import get_all_products_query


@jwt_required()
def cart_checkout():
    user = get_jwt_identity()
    user = UserModel.query.get(user["user_id"])
    address = user.addresses

    if not address:
        return {"error": "user must have an address"}, 400

    cart_products = CartsProductsModel.query.filter_by(cart_id=user.cart.cart_id).all()

    if not cart_products:
        return {"error": "user's cart is empty"}, 400

    new_order = OrdersModel(
        user_id=user.user_id,
        timestamp=datetime.now(),
        address_id=address[0].address_id,
        total=user.cart.total,
    )

    for product in cart_products:
        order_product = OrdersProductsModel(product_id=product.product_id)
        order_product.order = new_order
        db.session.add(order_product)

    actual_cart = (
        db.session.query(CartsProductsModel).filter_by(cart_id=user.cart.cart_id).all()
    )

    for item in actual_cart:
        db.session.delete(item)

    user.cart.total = 0

    try:
        db.session.commit()
    except:
        db.session.close()
        raise

    return jsonify(new_order), HTTPStatus.CREATED


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

        return {"msg": "Product has been delete from cart!"}, HTTPStatus.OK
    except NotFound as err:
        return {"error": err.description}, HTTPStatus.NOT_FOUND


@jwt_required()
def get_cart():
    user_id = get_jwt_identity()["user_id"]
    try:
        cart: Query = CartsModel.query.filter_by(user_id=user_id).first_or_404(
            description="Cart not found!"
        )
    except NotFound:
        return {"error": "Cart does not exists!"}, HTTPStatus.NOT_FOUND

    products = get_all_products_query(
        CartsModel, CartsProductsModel, CartsProductsModel.cart_id, cart.cart_id
    )

    cart_asdict = cart.asdict()
    cart_asdict["products"] = products
    return jsonify(cart_asdict), HTTPStatus.OK
