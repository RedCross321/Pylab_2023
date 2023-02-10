#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
    'Мыло': '56789',
    'Молоток': '54321',
    'Топор': '65432',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
    '56789': [
        {'quantity': 30, 'price': 105},
        {'quantity': 12, 'price': 95},
    ],
    '54321': [
        {'quantity': 1, 'price': 0},
    ],
    '65432': [
        {'quantity': 1, 'price': 20},
    ],    
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_quantity = store[goods['Лампа']][0]['quantity']
lamps_cost = lamps_quantity * store[goods['Лампа']][0]['price']


table_quantity = store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']
table_cost = table_quantity * store[goods['Стол']][0]['price']


sofa_quantity = store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']
sofa_cost = sofa_quantity * store[goods['Диван']][0]['price']


chair_quantity = store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] + store[goods['Стул']][2]['quantity']
chair_cost = chair_quantity * store[goods['Стул']][0]['price']


soap_quantity = store[goods['Мыло']][0]['quantity'] + store[goods['Мыло']][1]['quantity']
soap_cost = soap_quantity * store[goods['Мыло']][0]['price']


hammer_quantity = store[goods['Молоток']][0]['quantity']
hammer_cost = hammer_quantity * store[goods['Молоток']][0]['price']


axe_quantity = store[goods['Топор']][0]['quantity']
axe_cost = axe_quantity * store[goods['Топор']][0]['price']

# или проще (/сложнее ?)

print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')
print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')
print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')
print('Мыло -', soap_quantity, 'шт, стоимость', soap_cost, 'руб')
print('Молоток -', hammer_quantity, 'шт, стоимость', hammer_cost, 'руб')
print('Топор -', axe_quantity, 'шт, стоимость', axe_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
