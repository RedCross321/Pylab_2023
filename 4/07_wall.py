#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (600, 600)


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич



for g in range(600, 0, -50):
    if g % 100 == 50:
        k = 0
    else:
        k = -50
    for i in range(k, 600, 100):
        sd.rectangle(left_bottom = sd.Point(i, g-50), right_top = sd.Point(i+100, g), width=1)





sd.pause()