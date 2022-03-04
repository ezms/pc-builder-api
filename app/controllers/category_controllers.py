from http import HTTPStatus

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
            return {"Error": "The value must be string!"}, HTTPStatus.BAD_REQUEST

        data["name"] = data["name"].title()

        category = CategoryModel(**data)

        session.add(category)
        session.commit()

        return jsonify(category), HTTPStatus.CREATED

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            return {"Error": "Category already exists!"}, HTTPStatus.CONFLICT

    except KeyError:
        return {
            "Error": "Missing the following key: name!"
        }, HTTPStatus.UNPROCESSABLE_ENTITY

    except TypeError:
        return {"Error": "The valid key is only name!"}, HTTPStatus.CONFLICT

def get_all_categories():
    session = db.session

    categories = CategoryModel.query.all()

    return jsonify(categories), HTTPStatus.OK