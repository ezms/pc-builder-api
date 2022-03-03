from dataclasses import dataclass
from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.database import db


@dataclass
class UserAddress(db.Model):
    user_address_id: int
    address_id: int
    user_id: int

    __tablename__ = "users_addresses"

    user_address_id = Column(Integer, primary_key=True)
    address_id = Column(Integer, ForeignKey("addresses.address_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
