from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from app.core.database import db


@dataclass
class User(db.Model):
    user_id: int
    name: str
    email: str
    password: str
    cpf: str

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    email = Column(String(), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
