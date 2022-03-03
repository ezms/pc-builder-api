from dataclasses import dataclass

from sqlalchemy.orm import relationship, backref

from sqlalchemy import Column, Integer, String

from app.core.database import db


@dataclass
class UserModel(db.Model):

    __tablename__ = "users"

    user_id: int = Column(Integer, primary_key=True)
    name: str = Column(String(), nullable=False)
    email: str = Column(String(), unique=True, nullable=False)
    password: str = Column(String(100), nullable=False)
    cpf: str = Column(String(11), nullable=False, unique=True)

    addresses: list = relationship(
        "AddressModel", secondary="users_addresses", backref=backref("users")
    )

    orders: list = relationship("OrdersModel", backref=backref("user", uselist=False))
