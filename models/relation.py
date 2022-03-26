from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Relation(Base):
    __tablename__ = 'relation'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("service.id"))
    child_id = Column(Integer, ForeignKey("service.id"))

    def __init__(self, parent_id: int, child_id: int):
        self.parent_id = parent_id
        self.child_id = child_id

    def __repr__(self):
        return f'Связь [Родительский номер: {self.parent_id},  Наследующий номер: {self.child_id}]'

