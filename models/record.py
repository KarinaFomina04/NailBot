from sqlalchemy import Column, Integer, ForeignKey

from models.database import Base


class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    service_id = Column(Integer, ForeignKey("service.id"))
    time = Column(Integer)

    def __init__(self, user_id: int, service_id: int, time: int):
        self.user_id = user_id
        self.service_id = service_id
        self.time = time

    def __repr__(self):
        return f'Запись [Номер пользователя: {self.user_id}, Номер записи: {self.service_id}, Время: {self.time}]'