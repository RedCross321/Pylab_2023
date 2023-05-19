from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.database import Base


class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    type_food = Column(String)
    fabricator = Column(String)
    name = Column(String)
    price = Column(Integer)
    animal = relationship('Animal')


    def __repr__(self):
        return f'Корм [ID: {self.id},\
        Вид: {self.type_food}, Изготовитель: {self.fabricator}, Название: {self.name}, Цена: {self.price}]'