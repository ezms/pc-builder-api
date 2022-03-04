from datetime import timedelta
from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import create_access_token
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import DataError, IntegrityError

from app.core.database import db
from app.models.user_model import UserModel


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
