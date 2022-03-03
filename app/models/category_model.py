from dataclasses import asdict, dataclass

from sqlalchemy import Column, Integer, String

from app.core.database import db


@dataclass
class CategoryModel(db.Model):

    __tablename__ = "categories"

    category_id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False, unique=True)

    def asdict(self):
        return asdict(self)
