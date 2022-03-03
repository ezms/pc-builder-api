from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from app.core.database import db
from app.models.category_model import CategoryModel


def create_category():
    session = db.session
    data = request.get_json()

    try:

        if not type(data["name"]) == str:
            return {"Error": "The value must be string!"}, 400

        data["name"] = data["name"].title()

        category = CategoryModel(**data)

        session.add(category)
        session.commit()

        return jsonify(category), 201

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            return {"Error": "Category already exists!"}, 409

    except KeyError:
        return {"Error": "Missing the following key: name!"}, 409
