from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base

association_table = Table('association', Base.metadata,
                          Column('species_id', Integer, ForeignKey('species.id')),
                          Column('food_id', Integer, ForeignKey('food.id'))
                          )

class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    species_name = Column(String)
    foods = relationship('Food', secondary=association_table, backref='group_species')

    def __repr__(self):
        return f'Вид животного [ID: {self.id}, Название: {self.species_name}]'