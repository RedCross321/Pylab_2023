#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить список всех живущих на районе (пакет district) и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
from district.central_street.house1 import room1 as r1h1cs, room2 as r2h1cs
from district.central_street.house2 import room1 as r1h2cs, room2 as r2h2cs
from district.soviet_street.house1 import room1 as r1h1ss, room2 as r2h1ss
from district.soviet_street.house2 import room1 as r1h2ss, room2 as r2h2ss

rooms = [
    r1h1cs.folks, 
    r2h1cs.folks, 
    r1h2cs.folks, 
    r2h2cs.folks, 
    r1h1ss.folks, 
    r2h1ss.folks, 
    r1h2ss.folks, 
    r2h2ss.folks,
]

roomfolks = []
for x in rooms:
    roomfolks.extend(x)

print("На районе живут:", ', '.join(roomfolks))