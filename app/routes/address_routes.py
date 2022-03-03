from flask import Blueprint


bp_address = Blueprint("blueprint_address", __name__, url_prefix="/address")

# TODO: criar e importar funções JÁ DEFINIDAS no controller
# PHANTOM FUNCTIONS
def create_address():
    ...

def get_addresses():
    ...

def update_address():
    ...

def delete_address():
    ...


bp_address.post("")(create_address)
bp_address.get("")(get_addresses)
bp_address.patch("")(update_address)
bp_address.delete("")(delete_address)

