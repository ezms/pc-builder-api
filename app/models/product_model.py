from dataclasses import asdict, dataclass

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import backref, relationship

from app.core.database import db


@dataclass
class ProductModel(db.Model):

    __tablename__ = "products"

    product_id: int = Column(Integer, primary_key=True)
    model: str = Column(String, nullable=False)
    img: str = Column(String, nullable=False)
    price: float = Column(Float(2), nullable=False)
    description: str = Column(Text, nullable=True)

    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)

    def asdict(self):
        return asdict(self)

    category = relationship(
        "CategoryModel", backref=backref("products", uselist=True), uselist=False
    )
    cart = relationship(
        "CartModel",
        secondary="carts_products",
        backref=backref("products", uselist=True),
        uselist=False,
    )
    order = relationship(
        "OrderModel",
        secondary="orders_products",
        backref=backref("products", uselist=True),
        uselist=False,
    )
