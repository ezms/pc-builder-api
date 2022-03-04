from http import HTTPStatus

from flask import jsonify, request
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
