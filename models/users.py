from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from models.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=False)
    visit_count = Column(Integer)

    def __init__(self, id_: int, visit_count: int):
        self.id = id_
        self.visit_count = visit_count

    def __repr__(self):
        return f'Пользователь [Номер пользователя: {self.id}, Количество посещений: {self.visit_count}]'
