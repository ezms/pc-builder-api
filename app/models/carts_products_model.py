from dataclasses import asdict, dataclass

from sqlalchemy import Column, ForeignKey, Integer

from app.core.database import db


@dataclass
class CartsProductsModel(db.Model):
    __tablename__ = "carts_products"

    cart_product_id: int = Column(Integer, primary_key=True)
    cart_id: int = Column(Integer, ForeignKey("carts.cart_id"), nullable=False)
    product_id: int = Column(Integer, ForeignKey("products.product_id"))

    def asdict(self):
        return asdict(self)
