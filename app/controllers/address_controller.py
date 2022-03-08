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
        if type(data["cep"]) != str:
            return {"error": "CEP must be of String(str) type!"}, HTTPStatus.BAD_REQUEST

        if len(data["cep"]) != 8:
            raise ExpectationFailed(
                description="CEP field must contain only 8 characters!"
            )

        if type(data["numero"]) != int:
            return {
                "error": "House number must be of Integer type!"
            }, HTTPStatus.BAD_REQUEST

        if type(data["cidade"]) != str:
            raise ExpectationFailed(description="cidade must be of String(str) type!")

        if type(data["estado"]) != str:
            raise ExpectationFailed(description="estado must be of String(str) type!")

        if type(data["logradouro"]) != str:
            raise ExpectationFailed(
                description="logradouro must be of String(str) type!"
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
    except KeyError:
        return {
            "message": "Missing or invalid key(s)",
            "required keys": ["zip_code", "state", "city", "public_place", "number"],
            "recieved": list(data.keys()),
        }, HTTPStatus.BAD_REQUEST
    except ExpectationFailed as err:
        return {"error": err.description}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_address():
    current_user = get_jwt_identity()

    try:
        query = (
            db.session.query(AddressModel)
            .select_from(AddressModel)
            .join(UserAddressModel)
            .join(UserModel)
            .filter(UserAddressModel.user_id == current_user["user_id"])
            .first_or_404()
        )
        return jsonify(query), HTTPStatus.OK
    except NotFound as e:
        return {"error": f"{e.description}"}, e.code


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
        ).first_or_404()

        for key, value in address_data_factory.items():
            setattr(filtered_address, key, value)

        db.session.add(filtered_address)
        db.session.commit()

        return {}, HTTPStatus.NO_CONTENT

    except BadRequest as e:
        return {"error": e.description}, e.code
    except NotFound as e:
        return {"error": f"{e.description}"}, e.code
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
