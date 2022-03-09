import os
from http import HTTPStatus
import os

from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest, NotFound

from app.core.database import db
from app.models.category_model import CategoryModel
from app.models.product_model import ProductModel
from app.services.products_services import (create_category, populate_category,
                                            populate_product)
from app.services.validate_body_service import validate_body


def create_product():
    session = db.session
    data = request.get_json()

    token = request.headers["Authorization"].split(" ")[1]

    if not token:
        return {"error": "missing admin token"}, HTTPStatus.BAD_REQUEST
    elif token != os.getenv("DATABASE_ADMIN_TOKEN"):
        return {"error": "invalid admin token"}, HTTPStatus.FORBIDDEN

    try:

        if not type(data["model"]) == str:
            return {"error": "The model must be string!"}, HTTPStatus.BAD_REQUEST
        if not type(data["img"]) == str:
            return {"error": "The img must be string!"}, HTTPStatus.BAD_REQUEST
        if not type(data["price"]) == float:
            return {"error": "The price must be float!"}, HTTPStatus.BAD_REQUEST
        if not type(data["description"]) == str:
            return {"error": "The description must be string!"}, HTTPStatus.BAD_REQUEST
        if not type(data["category"]) == str:
            return {"error": "The category must be string!"}, HTTPStatus.BAD_REQUEST

        data["category"] = data["category"].title()

        category = data.pop("category")

        category_model: CategoryModel = CategoryModel.query.filter_by(
            name=category
        ).first()

        if category_model == None:
            create_category(category)
            category_model: CategoryModel = CategoryModel.query.filter_by(
                name=category
            ).first()

        data["category_id"] = category_model.category_id

        product = ProductModel(**data)

        session.add(product)
        session.commit()

        return jsonify(product), HTTPStatus.CREATED

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            return {"error": "Product already exists!"}, HTTPStatus.CONFLICT

    except KeyError:
        missing_fields = [
            field
            for field in ["model", "img", "price", "description", "category"]
            if field not in data.keys()
        ]
        return {
            "available_fields": ["model", "img", "price", "description", "category"],
            "missing_fields": missing_fields,
        }, HTTPStatus.UNPROCESSABLE_ENTITY

    except TypeError:
        return {"error": "The valid key is only model!"}, HTTPStatus.CONFLICT

    except NotFound as err:
        return {"error": err.description}, HTTPStatus.NOT_FOUND


def get_all_products():

    products = ProductModel.query.order_by(ProductModel.product_id).all()

    if products == []:
        populate_category()
        populate_product()
        products = ProductModel.query.order_by(ProductModel.product_id).all()

    return jsonify(products), HTTPStatus.OK


def get_product_by_id(id):

    product = ProductModel.query.filter_by(product_id=id).one_or_none()
    if product == None:
        return {"error": "Product not found!"}, HTTPStatus.NOT_FOUND

    return jsonify(product), HTTPStatus.OK


def update_product(id):
    session = db.session
    data = request.get_json()

    token = request.headers["Authorization"].split(" ")[1]

    if not token:
        return {"error": "missing admin token"}, HTTPStatus.BAD_REQUEST
    elif token != os.getenv("DATABASE_ADMIN_TOKEN"):
        return {"error": "invalid admin token"}, HTTPStatus.FORBIDDEN

    try:
        if not data:
            raise BadRequest(description="Request body cannot be empty")

        for key in data.keys():
            if key == "price":
                validate_body(data, price=int)
            elif key == "model":
                validate_body(data, model=str)
            elif key == "img":
                validate_body(data, img=str)
            elif key == "description":
                validate_body(data, description=str)

        product = ProductModel.query.filter_by(product_id=id).one_or_none()
        if product == None:
            return {"error": "Product not found!"}, HTTPStatus.NOT_FOUND

        for key, value in data.items():
            setattr(product, key, value)

        session.add(product)
        session.commit()

        return jsonify(product), HTTPStatus.OK

    except BadRequest as err:
        return {"error": err.description}, HTTPStatus.BAD_REQUEST


def delete_product(id):
    session = db.session

    token = request.headers["Authorization"].split(" ")[1]

    if not token:
        return {"error": "missing admin token"}, HTTPStatus.BAD_REQUEST
    elif token != os.getenv("DATABASE_ADMIN_TOKEN"):
        return {"error": "invalid admin token"}, HTTPStatus.FORBIDDEN

    product = ProductModel.query.filter_by(product_id=id).one_or_none()
    if product == None:
        return {"error": "Product not found!"}, HTTPStatus.NOT_FOUND

    session.delete(product)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
