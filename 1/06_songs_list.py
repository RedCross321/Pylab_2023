#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код

songs3 = violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[8][1] 
round(songs3, 2)
print("Три песни звучат %.2f минут"%songs3)

# Есть словарь песен группы Depeche Mode

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

violator_songs_sigma = [
    ['Pixies - where is my mind', 3.51],
    ['Huey Lewis & The News - Hip To Be Square', 3.52],
    ['College feat. Electric Youth - A Real Hero', 4.28],
    ['Gachimuchi will be fine', 2.24],
]

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код

another_songs3 = violator_songs_dict['Sweetest Perfection'] + violator_songs_dict['Policy of Truth'] + violator_songs_dict['Blue Dress']
round(another_songs3)
print("А другие три песни звучат %d минут"%another_songs3)

sigma_songs3 = violator_songs_sigma[0][1] + violator_songs_sigma[1][1] + violator_songs_sigma[2][1] + violator_songs_sigma[3][1]
print("А сигма песни звучат %.2f минут"%sigma_songs3)