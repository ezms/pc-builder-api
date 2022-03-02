from sqlalchemy import Column, Float, DateTime, ForeignKey, Integer
from dataclasses import asdict, dataclass

from app.core.database import db

@dataclass
class OrdersModel(db.Model):
    __tablename__ = "orders"

    order_id: int = Column(Integer, primary_key=True)
    total: float = Column(Float, nullable=False)
    timestamp: str = Column(DateTime, nullable=False)

    user_id: int = Column(Integer, ForeignKey("users.user_id"), nullable=True)

    def asdict(self):
        return asdict(self)
