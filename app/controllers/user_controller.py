from datetime import timedelta
from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import DataError, IntegrityError
from sqlalchemy.orm import Query
from werkzeug.exceptions import NotFound

from app.core.database import db
from app.models.carts_model import CartsModel
from app.models.order_model import OrdersModel
from app.models.order_product_model import OrdersProductsModel
from app.models.user_model import UserModel
from app.models.users_addresses_model import UserAddressModel


def create_user():
    data = request.get_json()

    try:
        user = UserModel(
            name=data["name"].lower().title(),
            email=data["email"].lower(),
            password=data["password"],
            cpf=data["cpf"],
        )

        db.session.add(user)

        user_query: Query = (
            db.session.query(UserModel.user_id)
            .filter(UserModel.cpf.like(data["cpf"]))
            .one()
        )

        cart_user_id = user_query.user_id

        cart = CartsModel(user_id=cart_user_id)

        db.session.add(cart)
        db.session.commit()

    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            return {"error": "'email' or 'cpf' already exists!"}, HTTPStatus.CONFLICT
    except DataError:
        return {
            "error": "'cpf' field must contain only 11 characters!"
        }, HTTPStatus.BAD_REQUEST
    except KeyError:
        missing_fields = [
            field
            for field in ["name", "email", "password", "cpf"]
            if field not in data.keys()
        ]
        return {
            "available_fields": ["name", "email", "password", "cpf"],
            "missing_fields": missing_fields,
        }, HTTPStatus.UNPROCESSABLE_ENTITY

    return jsonify(user), HTTPStatus.CREATED


def login():

    data = request.get_json()
    data = {key: val for key, val in data.items() if key in ["email", "password"]}

    missing_fields = [x for x in ["email", "password"] if x not in data.keys()]

    if missing_fields:
        return {"missing fields": missing_fields}, HTTPStatus.BAD_REQUEST

    for key, val in data.items():
        if type(val) is not str:
            return {"error": f"{{{key}}} value must be string"}, HTTPStatus.BAD_REQUEST

    email = data.get("email")
    password = data.get("password")

    user: UserModel = UserModel.query.filter_by(email=email.lower()).first()

    if not user:
        return {"error": "email not found"}, HTTPStatus.NOT_FOUND

    if user.verify_password(password):
        access_token = create_access_token(
            identity=user, expires_delta=timedelta(days=1)
        )
        return {"access_token": access_token}
    else:
        return {"error": "invalid password"}, HTTPStatus.FORBIDDEN


@jwt_required()
def get_user():
    current_user_token = request.headers.get("Authorization")
    current_user = get_jwt_identity()
    user = UserModel.query.get(current_user.get("user_id")).asdict()
    user.pop("password_hash")
    return jsonify(user)


@jwt_required()
def delete_user():
    try:
        user_id = get_jwt_identity()["user_id"]

        user: Query = UserModel.query.get_or_404(
            user_id, description="User not found on database!"
        )

        cart: Query = CartsModel.query.filter_by(user_id=user_id).first_or_404(
            description="User cart not found on database!"
        )

        orders: Query = OrdersModel.query.filter_by(user_id=user_id).all()

        addressess: Query = UserAddressModel.query.filter_by(user_id=user_id).all()

        for address in addressess:
            db.session.delete(address)

        for order in orders:
            order_id = order.order_id

            order_product: Query = OrdersProductsModel.query.filter_by(
                order_id=order_id
            ).all()

            for op in order_product:
                db.session.delete(op)

            db.session.delete(order)

        db.session.delete(cart)
        db.session.delete(user)
        db.session.commit()

        return {"msg": f"User {user.name} has been deleted from the database"}

    except NotFound as err:
        return {"error": err.description}, 404
