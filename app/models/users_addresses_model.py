from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey, Integer

from app.core.database import db


@dataclass
class UserAddressModel(db.Model):

    __tablename__ = "users_addresses"

    __mapper_args__ = {"confirm_deleted_rows": False}

    user_address_id: int = Column(Integer, primary_key=True)
    address_id: int = Column(Integer, ForeignKey("addresses.address_id"))
    user_id: int = Column(Integer, ForeignKey("users.user_id"))
