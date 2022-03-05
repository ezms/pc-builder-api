from http import HTTPStatus

from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.core.database import db
from app.models.address_model import AddressModel


@jwt_required()
def create_address():
    data = request.get_json()
    
    try:
        if type(data["cep"]) != str:
            return {"error": "CEP must be of String(str) type!"}, HTTPStatus.BAD_REQUEST

        if type(data["numero"]) != int:
            return {"error": "House number must be of Integer type!"}, HTTPStatus.BAD_REQUEST

        address_data_factory = {
            "zip_code": data["cep"],
            "state": data["estado"],
            "city": data["cidade"],
            "public_place": data["logradouro"],
            "number": data["numero"],
        }

        db.session.add(AddressModel(**address_data_factory))
        db.session.commit()

        return address_data_factory, HTTPStatus.CREATED
    except KeyError:
        return {
            "message": "Missing or invalid key(s)",
            "required Keys": ["zip_code", "state", "city", "public_place", "number"],
            "recieved": list(data.keys())
        }, HTTPStatus.BAD_REQUEST
    


@jwt_required()
def get_address():
    current_user = get_jwt_identity()
    print(get_jwt_identity())

    query = db.session.query()
    return {}, 200

def update_address():
    ...
