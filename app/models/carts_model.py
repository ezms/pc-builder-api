from dataclasses import asdict, dataclass

from sqlalchemy import Column, Float, ForeignKey, Integer

from app.core.database import db


@dataclass
class CartsModel(db.Model):
    __tablename__ = "carts"

    cart_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    total: float = Column(Float, default=0)

    def asdict(self):
        return asdict(self)
