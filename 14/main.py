import os

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session as SQLSession

from models.database import DATABASE_NAME, Session
import create_database as db_creator
from models.species import Species, association_table
from models.food import Food
from models.animal import Animal

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session: SQLSession = Session()

    animal_query = session.query(Animal.id, Animal.nickname, Animal.floor, Animal.birthdate, Food.name, Food.price).join(Food)
    print('--------------------------------')
    print('Запрос 1 - все животные')
    print('--------------------------------')
    for it in animal_query:
        print(*it)
    print('--------------------------------')
    print('Запрос 2 - все корма')
    print('--------------------------------')
    for i in range(1, 6):
        food_query = session.query(Animal).join(Food).filter(Food.id == i)
        print(*session.query(Food.name).filter(Food.id == i).first(), f'- {food_query.count()} животных едят это')
        
    session.close()
