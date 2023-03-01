#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает ингридиентов - создать соответствующие функции в модуле my_burger

import my_burger as mb

print()
def recipe_double_cheeseburger():
    mb.add_nude_bun()
    mb.add_cutlet()
    mb.add_cheese()
    mb.add_cutlet()
    mb.add_cheese()
    mb.add_cucumber()
    mb.add_tomato()
    mb.add_mayonnaise()
    mb.add_seasoning()
    mb.add_bun()

def recipe_my_burg():
    mb.add_nude_bun()
    mb.add_mayonnaise()
    mb.add_cutlet()
    mb.add_cheese()
    mb.add_cheese()
    mb.add_cheese()
    mb.add_cutlet()
    mb.add_cucumber()
    mb.add_seasoning()
    mb.add_bun()

print("Все ингредиенты: ", ', '.join(mb.ingredients))
print()
answer = input("Введите 'Чиз' для рецепта двойного чизбургера или 'Мешанина' для рецепта моего собственного бургера >> ")
if answer == 'Чиз':
    print()
    recipe_double_cheeseburger()
elif answer == 'Мешанина':
    print()
    recipe_my_burg()
else:
    print()
    print('Ты по-мойму букавы перепуткал')
