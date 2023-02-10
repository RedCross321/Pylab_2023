#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код

for i in range (5, 20, 5):
    sd.circle(center_position = sd.Point(50, 550),radius=i)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код

s = sd.random_point()
for i in range (5, 20, 5):
    sd.circle(center_position = s,radius=i,color=sd.random_color(), width=1)

# # Нарисовать 10 пузырьков в ряд
# # TODO здесь ваш код


for i in range (5, 20, 5):
    for g in range(50, 400, 35):
        sd.circle(center_position = sd.Point(g, 500),radius=i)

# # Нарисовать три ряда по 10 пузырьков
# # TODO здесь ваш код

for i in range (5, 20, 5):
    for g in range(50, 400, 35):
        for k in range(400, 250, -50):
            sd.circle(center_position = sd.Point(g, k),radius=i)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код


for _ in range(1,101):
    d = sd.random_point()
    for i in range (5, 20, 5):
        sd.circle(center_position = d,radius=i,color=sd.random_color())

sd.pause()
