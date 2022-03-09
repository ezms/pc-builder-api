import os
from http import HTTPStatus

from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from app.core.database import db
from app.models.category_model import CategoryModel
from app.models.product_model import ProductModel
from app.services.products_query_services import get_products_for_category
from app.services.validate_body_service import validate_body


def create_category():
    session = db.session
    data = request.get_json()

    token = request.headers["Authorization"].split(" ")[1]

    if not token:
        return {"error": "missing admin token"}, HTTPStatus.BAD_REQUEST
    elif token != os.getenv("DATABASE_ADMIN_TOKEN"):
        return {"error": "invalid admin token"}, HTTPStatus.FORBIDDEN

    try:

        validate_body(data, name=str)

        data["name"] = data["name"].title()

        category = CategoryModel(**data)

        session.add(category)
        session.commit()

        return jsonify(category), HTTPStatus.CREATED

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            return {"error": "Category already exists!"}, HTTPStatus.CONFLICT

    except BadRequest as err:
        return {"error": err.description}, HTTPStatus.BAD_REQUEST


def get_all_categories():
    session = db.session

    categories = CategoryModel.query.order_by(CategoryModel.category_id).all()

    return jsonify(categories), HTTPStatus.OK


def get_category_by_id(id):
    session = db.session

    category = CategoryModel.query.filter_by(category_id=id).one_or_none()
    if category == None:
        return {"error": "Category not found!"}, HTTPStatus.NOT_FOUND

    products = get_products_for_category(
        CategoryModel, id, ProductModel.category_id, CategoryModel.category_id
    )

    category_asdict = category.asdict()
    category_asdict["products"] = products

    return jsonify(category_asdict), HTTPStatus.OK


def update_category(id):
    session = db.session
    data = request.get_json()

    token = request.headers["Authorization"].split(" ")[1]

    if not token:
        return {"error": "missing admin token"}, HTTPStatus.BAD_REQUEST
    elif token != os.getenv("DATABASE_ADMIN_TOKEN"):
        return {"error": "invalid admin token"}, HTTPStatus.FORBIDDEN

    try:
        validate_body(data, name=str)

        category = CategoryModel.query.filter_by(category_id=id).one_or_none()
        if category == None:
            return {"error": "Category not found!"}, HTTPStatus.NOT_FOUND

        for key, value in data.items():
            setattr(category, key, value)

        session.add(category)
        session.commit()

        return jsonify(category), HTTPStatus.OK

    except BadRequest as err:
        return {"error": err.description}, HTTPStatus.BAD_REQUEST


def delete_category(id):
    session = db.session

    token = request.headers["Authorization"].split(" ")[1]

    if not token:
        return {"error": "missing admin token"}, HTTPStatus.BAD_REQUEST
    elif token != os.getenv("DATABASE_ADMIN_TOKEN"):
        return {"error": "invalid admin token"}, HTTPStatus.FORBIDDEN

    category = CategoryModel.query.filter_by(category_id=id).one_or_none()
    if category == None:
        return {"error": "Category not found!"}, HTTPStatus.NOT_FOUND

    session.delete(category)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
