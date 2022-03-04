from http import HTTPStatus

from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import DataError, IntegrityError

from app.core.database import db
from app.models.carts_model import CartsModel
from app.models.user_model import UserModel

from sqlalchemy.orm import Query


def create_user():
    data = request.get_json()

    try:
        user = UserModel(
            name=data["name"].lower().title(),
            email=data["email"].lower(),
            password=data["password"],
            cpf=data["cpf"],
        )

        print('*'*100)
        print(user)
        print('*'*100)

        db.session.add(user)
        db.session.commit()

        user_query: Query = db.session.query(UserModel.user_id).filter_by(UserModel.cpf.like(data["cpf"])).one()

        cart_user_id = user_query.user_id

        cart = CartsModel(
            user_id = cart_user_id
        )

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
