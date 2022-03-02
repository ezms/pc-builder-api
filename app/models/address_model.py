from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey, Integer, String

from app.core.database import db


@dataclass
class AddressModel(db.Model):
    __tablename__ = "addresses"

    address_id = Column(Integer, primary_key=True)
    zip_code = Column(String(8), nullable=False) # CEP
    state = Column(String(15), nullable=False)
    city = Column(String(50), nullable=False)
    public_place = Column(String(60), nullable=False)
    number = Column(Integer, nullable=False)

    order_id = Column(Integer, ForeignKey("orders.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
