from dataclasses import asdict, dataclass

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.database import db


@dataclass
class OrdersProductsModel(db.Model):
    __tablename__ = "orders_products"

    order_product_id: int = Column(Integer, primary_key=True)

    order_id: int = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    product_id: int = Column(Integer, ForeignKey("products.product_id"), nullable=False)

    order = relationship("OrdersModel", uselist=False)

    def asdict(self):
        return asdict(self)
