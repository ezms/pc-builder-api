from datetime import timedelta
from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import create_access_token

from app.core.database import db
from app.models.user_model import UserModel


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
