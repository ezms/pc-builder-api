from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import BadRequest, ExpectationFailed, NotFound

from app.core.database import db
from app.models.address_model import AddressModel
from app.models.user_model import UserModel
from app.models.users_addresses_model import UserAddressModel
from app.services.validate_body_service import validate_body


@jwt_required()
def create_address():
    current_user = get_jwt_identity()
    data = request.get_json()

    try:
        validate_body(data, cep=str, estado=str, cidade=str, logradouro=str, numero=int)

        if len(data["cep"]) != 8:
            raise ExpectationFailed(
                description="CEP field must contain only 8 characters!"
            )

        address_data_factory = {
            "zip_code": data["cep"],
            "state": data["estado"],
            "city": data["cidade"],
            "public_place": data["logradouro"],
            "number": data["numero"],
        }

        address = AddressModel(**address_data_factory)

        db.session.add(address)
        db.session.commit()

        users_addresses = UserAddressModel(
            user_id=current_user["user_id"], address_id=address.address_id
        )

        db.session.add(users_addresses)
        db.session.commit()

        return address_data_factory, HTTPStatus.CREATED
    except BadRequest as err:
        return {"error": err.description}, HTTPStatus.UNPROCESSABLE_ENTITY
    except ExpectationFailed as err:
        return {"error": err.description}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_address():
    current_user = get_jwt_identity()

    query = (
        db.session.query(AddressModel)
        .select_from(AddressModel)
        .join(UserAddressModel)
        .join(UserModel)
        .filter(UserAddressModel.user_id == current_user["user_id"])
        .all()
    )
    return jsonify(query), HTTPStatus.OK


@jwt_required()
def update_address(address_id: int):

    user = get_jwt_identity()
    data = request.get_json()

    address = UserAddressModel.query.filter_by(
        address_id=address_id, user_id=user["user_id"]
    ).first()

    try:

        if not address:
            raise NotFound(description="address not found!")

        validate_body(data, cep=str, cidade=str, estado=str, logradouro=str, numero=int)

        if len(data["cep"]) != 8:
            raise ExpectationFailed(
                description="CEP field must contain only 8 characters!"
            )

        address_data_factory = {
            "zip_code": data["cep"],
            "state": data["estado"],
            "city": data["cidade"],
            "public_place": data["logradouro"],
            "number": data["numero"],
        }

        filtered_address = AddressModel.query.filter_by(
            address_id=address_id
        ).first_or_404(description="Address id not found on database!")

        for key, value in address_data_factory.items():
            setattr(filtered_address, key, value)

        db.session.add(filtered_address)
        db.session.commit()

        return {}, HTTPStatus.NO_CONTENT
    except NotFound as err:
        return {"error": err.description}, err.code
    except BadRequest as err:
        return {"error": err.description}, HTTPStatus.UNPROCESSABLE_ENTITY
    except ExpectationFailed as err:
        return {"error": err.description}, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_address(address_id: int):
    try:
        filtered_address = AddressModel.query.filter_by(
            address_id=address_id
        ).first_or_404(description="Address id not found on database!")

        db.session.delete(filtered_address)
        db.session.commit()

        return {}, HTTPStatus.NO_CONTENT
    except NotFound as e:
        return {"error": f"{e.description}"}, e.code
