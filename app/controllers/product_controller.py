from http import HTTPStatus
from http.client import OK

from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from app.core.database import db
from app.models.category_model import CategoryModel
from app.models.product_model import ProductModel
from app.services.products_services import populate_category, populate_product


def create_product():
    session = db.session
    data = request.get_json()

    try:

        if not type(data["model"]) == str:
            return {"Error": "The model must be string!"}, HTTPStatus.BAD_REQUEST
        if not type(data["img"]) == str:
            return {"Error": "The img must be string!"}, HTTPStatus.BAD_REQUEST
        if not type(data["price"]) == float:
            return {"Error": "The price must be float!"}, HTTPStatus.BAD_REQUEST
        if not type(data["description"]) == str:
            return {"Error": "The description must be string!"}, HTTPStatus.BAD_REQUEST
        if not type(data["category"]) == str:
            return {"Error": "The category must be string!"}, HTTPStatus.BAD_REQUEST

        data["category"] = data["category"].title()

        category = data.pop("category")

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
            return {"Error": "Product already exists!"}, HTTPStatus.CONFLICT

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
        return {"Error": "The valid key is only model!"}, HTTPStatus.CONFLICT


def get_all_products():

    products = ProductModel.query.order_by(ProductModel.product_id).all()
    print(products)
    if products == []:
        populate_category()
        populate_product()
        products = ProductModel.query.order_by(ProductModel.product_id).all()


    return jsonify(products), HTTPStatus.OK


def get_product_by_id(id):

    product = ProductModel.query.filter_by(product_id=id).one_or_none()
    if product == None:
        return {"Error": "Product not founded!"}, HTTPStatus.NOT_FOUND

    return jsonify(product), HTTPStatus.OK


def update_product(id):
    session = db.session
    data = request.get_json()

    product = ProductModel.query.filter_by(product_id=id).one_or_none()
    if product == None:
        return {"Error": "Product not founded!"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()

    return jsonify(product), HTTPStatus.OK


def delete_product(id):
    session = db.session

    product = ProductModel.query.filter_by(product_id=id).one_or_none()
    if product == None:
        return {"Error": "Product not founded!"}, HTTPStatus.NOT_FOUND

    session.delete(product)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
