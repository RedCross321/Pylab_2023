from sqlalchemy import Column, Integer, String, ForeignKey

from models.database import Base


class Animal(Base):
    __tablename__ = 'animal'

    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    birthdate = Column(String)
    floor = Column(String)
    food = Column(Integer, ForeignKey('food.id'))

    def __init__(self, nickname: str, birthdate: str, floor: str, id_food: int):
        self.nickname = nickname
        self.birthdate = birthdate
        self.floor = floor
        self.food = id_food

    def __repr__(self):
        info: str = f'Животное [Кличка: {self.nickname}, ' \
            f'Дата рождения: {self.birthdate}, Пол: {self.floor}, ID корма: {self.food}]'
        return info