from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.core.database import db
from app.models.order_model import OrdersModel
from app.models.order_product_model import OrdersProductsModel
from app.models.product_model import ProductModel
from sqlalchemy.orm import Query

@jwt_required
def get_user_orders():
    orders = get_jwt_identity()['orders']

    # return jsonify(orders), 200

############################################

    user_id = get_jwt_identity()['id']

    order_query: Query = db.session.query(OrdersModel).filter(OrdersModel.user_id.like(user_id)).all()