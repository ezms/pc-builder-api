from dataclasses import asdict, dataclass

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text

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
