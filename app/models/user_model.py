from dataclasses import dataclass

from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.orm import relationship, backref

from sqlalchemy import Column, Integer, String

from app.core.database import db


@dataclass
class UserModel(db.Model):

    __tablename__ = "users"

    user_id: int = Column(Integer, primary_key=True)
    name: str = Column(String(), nullable=False)
    email: str = Column(String(), unique=True, nullable=False)
    password_hash: str = Column(String(100), nullable=False)
    cpf: str = Column(String(11), nullable=False, unique=True)

    addresses: list = relationship(
        "AddressModel", secondary="users_addresses", backref=backref("users")
    )

    orders: list = relationship("OrdersModel", backref=backref("user", uselist=False))

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
