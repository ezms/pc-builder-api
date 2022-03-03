from http import HTTPStatus

from flask import jsonify, request

from app.core.database import db
from app.models.user_model import UserModel


def create_user():
    data = request.get_json()

    user = UserModel(
        name=data["name"],
        email=data["email"],
        password=data["password"],
        cpf=data["password"],
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(user), HTTPStatus.CREATED
