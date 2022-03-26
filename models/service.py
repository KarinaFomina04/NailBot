from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.database import Base


class Service(Base):
    __tablename__ = "service"

    id = Column(Integer, primary_key=True)
    name_service = Column(String)
    price = Column(Integer, nullable=True)
    price_from = Column(Integer, nullable=True)
    price_to = Column(Integer, nullable=True)

    def __init__(self, name_service: str,  price: int, price_from: int = None, price_to: int = None):
        self.name_service = name_service
        self.price = price
        self.price_from = price_from
        self.price_to = price_to

    def __repr__(self):
        return f'Сервис [Название: {self.name_service}, Цена: {self.price}]'
