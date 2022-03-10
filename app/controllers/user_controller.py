from datetime import timedelta
from http import HTTPStatus
from os import getenv

import sqlalchemy
from flask import current_app, jsonify, render_template, request, url_for
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)
from flask_mail import Message
from itsdangerous import BadTimeSignature, SignatureExpired
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import DataError, IntegrityError
from sqlalchemy.orm import Query
from werkzeug.exceptions import BadRequest, ExpectationFailed, NotFound

from app.core.database import db
from app.core.email import secret_url
from app.models.address_model import AddressModel
from app.models.carts_model import CartsModel
from app.models.order_model import OrdersModel
from app.models.order_product_model import OrdersProductsModel
from app.models.user_model import UserModel
from app.models.users_addresses_model import UserAddressModel
from app.services.validate_body_service import validate_body


def register():
    data = request.get_json()

    try:

        validate_body(data, name=str, email=str, cpf=str, password=str)

        if len(data["cpf"]) != 11:
            raise ExpectationFailed(
                description="'cpf' field must contain only 11 characters!"
            )

        user = UserModel(
            name=data["name"].lower().title(),
            email=data["email"].lower(),
            password=data["password"],
            cpf=data["cpf"],
        )

        email = data["email"]
        token = secret_url.dumps(email, salt="email-confirm")
        link = url_for("api.blueprint_user.confirm_email", token=token, _external=True)

        msg = Message(
            subject="Confirm your Email",
            sender=["PC Builder", getenv("MAIL_USERNAME")],
            recipients=[email],
            html=render_template(
                "email_validation.html", name=data["name"].title(), link=link
            ),
        )

        current_app.mail.send(msg)

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
    except ExpectationFailed as err:
        return {"error": err.description}, HTTPStatus.BAD_REQUEST
    except BadRequest as err:
        return err.description, HTTPStatus.UNPROCESSABLE_ENTITY

    user_asdict = user.asdict()
    user_asdict["cart"] = user.cart.asdict()
    user_asdict["cart"]["products"] = user.cart.products

    return jsonify(user_asdict), HTTPStatus.CREATED


def confirm_email(token):
    try:
        email = secret_url.loads(token, salt="email-confirm", max_age=3600)

        filtered_user = (
            db.session.query(UserModel)
            .filter_by(email=email)
            .first_or_404(description=f"Email {email} not found on database!")
        )

        fields_to_update = {"confirmed_email": True}

        for key, value in fields_to_update.items():
            setattr(filtered_user, key, value)

        db.session.add(filtered_user)
        db.session.commit()

        return render_template("redirect_to_store.html"), HTTPStatus.OK
    except NotFound as err:
        return {"error": err.description}, HTTPStatus.NOT_FOUND
    except SignatureExpired:
        return {"error": "The token is expired!"}
    except BadTimeSignature:
        return {"error": "Invalid token!"}


def login():

    data = request.get_json()

    try:
        validate_body(data, email=str, password=str)
    except BadRequest as err:
        return err.description, HTTPStatus.UNPROCESSABLE_ENTITY

    email = data.get("email")
    password = data.get("password")

    try:
        user: UserModel = UserModel.query.filter_by(email=email.lower()).first_or_404()

    except NotFound:
        return {"error": "email not found"}, HTTPStatus.NOT_FOUND

    if not user.confirmed_email:
        return {"error": "Email is not verified"}, HTTPStatus.UNAUTHORIZED

    if user.verify_password(password):
        access_token = create_access_token(
            identity=user, expires_delta=timedelta(days=1)
        )
        return {"access_token": access_token}
    else:
        return {"error": "invalid password"}, HTTPStatus.FORBIDDEN


@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    try:
        user = UserModel.query.get(current_user.get("user_id")).asdict()
    except AttributeError:
        return {"error": "User not found on database!"}, HTTPStatus.NOT_FOUND
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
            address_query: Query = AddressModel.query.get(address.address_id)
            db.session.delete(address_query)
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

        return "", HTTPStatus.NO_CONTENT

    except NotFound as err:
        return {"error": err.description}, HTTPStatus.NOT_FOUND


@jwt_required()
def update_user():
    data = request.get_json()

    try:
        if not data:
            raise BadRequest(description="Request body cannot be empty")

    except BadRequest as err:
        return {"error": err.description}, HTTPStatus.BAD_REQUEST

    try:
        current_user = get_jwt_identity()
        user = UserModel.query.get(current_user["user_id"])

        data = {
            key: val
            for key, val in data.items()
            if key in ["email", "password", "cpf", "name"]
        }

        for val in data.values():
            if type(val) != str:
                invalid_values = [key for key in data.keys() if type(data[key]) != str]
                return {
                    "error": {
                        "available_fields": [
                            "name type should be string",
                            "email type should be string",
                            "cpf type should be string",
                            "password type should be string",
                        ],
                        "invalid_fields": invalid_values,
                    }
                }, HTTPStatus.BAD_REQUEST
            user.name = data.get("name") or user.name
            user.cpf = data.get("cpf") or user.cpf
            user.email = data.get("email") or user.email

        if data.get("password"):
            user.password = data.get("password")

            if "cpf" in data.keys():
                if len(data["cpf"]) != 11:
                    raise ExpectationFailed(
                        description="'cpf' field must contain only 11 characters!"
                    )
            db.session.commit()

        user_dict = {
            key: val
            for key, val in user.asdict().items()
            if key not in ["password_hash", "addresses", "orders"]
        }
    except sqlalchemy.exc.IntegrityError as e:
        db.session.close()
        if isinstance(e.orig, UniqueViolation):
            return (
                jsonify({"error": e.args[0][e.args[0].find("Key") : -2]}),
                HTTPStatus.CONFLICT,
            )
    except ExpectationFailed as err:
        return {"error": err.description}, HTTPStatus.BAD_REQUEST
    except AttributeError:
        return {"error": "User not found on database!"}, HTTPStatus.NOT_FOUND

    return jsonify(user_dict)
