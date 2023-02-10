#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (600, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.

pos_x = 50
pos_x1= 350
for g in rainbow_colors:
    sd.line(start_point = sd.Point(pos_x, 50), end_point = sd.Point(pos_x1, 450), color = g, width=4)
    pos_x += 5
    pos_x1 += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

rad = 600
for g in rainbow_colors:
    sd.circle(center_position = sd.Point(300, -300),radius=rad,color=g, width=10)
    rad -= 10


sd.pause()
