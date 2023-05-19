from faker import Faker

from models.database import create_db, Session
from models.animal import Animal
from models.food import Food
from models.species import Species


def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session: Session):
    species_names1 = ['Кот', 'Собака', 'Капибара',
                     'Крыса', 'Помойный енот', 'Угорь',
                     'Какаду']
    group_nickname = ['Рыжик', 'Толстяк', 'Картошка', 'Блохастый', 
                    'Дуня', 'Звездочка', 'Майор Игорь', 'Райан Гослинг', 'Барби Кен']
    floor_group = ['F', 'M']
    food1 = Food(type_food='Сухой', fabricator = 'Мяумаркет', name = 'Вискас', price = '120')
    food2 = Food(type_food='Влажный', fabricator = 'Петдаетс', name = 'Китекет', price = '170')
    food3 = Food(type_food='Паштет', fabricator = 'Рубис', name = 'Фролик', price = '132')
    food4 = Food(type_food='Зерновой', fabricator = 'Четвероногий гурман', name = 'Шеба', price = '76')
    food5 = Food(type_food='Травяной', fabricator = 'Норман', name = 'Педигри', price = '400')
    session.add(food1)
    session.add(food2)
    session.add(food3)
    session.add(food4)
    session.add(food5)

    faker = Faker('ru_RU')
    group_list = [food1, food2, food3, food4, food5]
    session.commit()
    for _ in range(50):
        nickname = faker.random.choice(group_nickname)
        birthdate = faker.date()
        floor = faker.random.choice(floor_group)
        food = faker.random.choice(group_list)
        animal = Animal(nickname, birthdate, floor, food.id)
        it = faker.random.choice(species_names1)
        species = Species(species_name=it)
        session.add(animal)
        session.add(species)


    session.commit()
    session.close()