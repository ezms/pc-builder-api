from flask import Blueprint
from app.controllers.address_controller import create_address, get_address, update_address, delete_address


bp_address = Blueprint("blueprint_address", __name__, url_prefix="/address")


bp_address.post("")(create_address)
bp_address.get("")(get_address)
bp_address.put("/<int:address_id>")(update_address)
bp_address.delete("/<int:address_id>")(delete_address)
