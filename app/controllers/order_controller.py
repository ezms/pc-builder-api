from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Query

from app.core.database import db
from app.models.order_model import OrdersModel


@jwt_required()
def get_orders():

    user_id = get_jwt_identity()["user_id"]

    order_query: Query = (
        db.session.query(OrdersModel).filter(OrdersModel.user_id == (user_id)).all()
    )

    return jsonify(order_query), 200
