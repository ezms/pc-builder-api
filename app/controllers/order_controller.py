from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Query
from werkzeug.exceptions import NotFound

from app.core.database import db
from app.models.order_model import OrdersModel
from app.models.order_product_model import OrdersProductsModel
from app.services.products_query_services import get_all_products_query


@jwt_required()
def get_orders():

    user_id = get_jwt_identity()["user_id"]

    order_query: Query = (
        db.session.query(OrdersModel).filter(OrdersModel.user_id == (user_id)).all()
    )

    return jsonify(order_query), 200


@jwt_required()
def get_order_by_id(order_id):

    user_id = get_jwt_identity()["user_id"]

    try:
        order: Query = OrdersModel.query.filter_by(
            order_id=order_id, user_id=user_id
        ).first_or_404(description="Order not found!")
    except NotFound:
        return {"error": "Order does not exists!"}, HTTPStatus.NOT_FOUND

    products = get_all_products_query(
        OrdersModel, OrdersProductsModel, OrdersProductsModel.order_id, order.order_id
    )

    order_asdict = order.asdict()
    order_asdict["products"] = products

    return jsonify(order_asdict), HTTPStatus.OK