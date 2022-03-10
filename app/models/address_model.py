from dataclasses import asdict, dataclass

from sqlalchemy import Column, ForeignKey, Integer, String

from app.core.database import db


@dataclass
class AddressModel(db.Model):
    __tablename__ = "addresses"

    address_id: int = Column(Integer, primary_key=True)
    zip_code: str = Column(String(8), nullable=False)  # CEP
    state: str = Column(String(15), nullable=False)
    city: str = Column(String(50), nullable=False)
    public_place: str = Column(String(60), nullable=False)
    number: int = Column(Integer, nullable=False)

    def asdict(self):
        return asdict(self)
