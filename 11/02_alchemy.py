# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if other == air:
            return  Storm(part1=self, part2=other)
        elif other == fire:
            return  Steam(part1=self, part2=other)
        elif other == ground:
            return  Dirt(part1=self, part2=other)



class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if other == water:
            return Storm(part1=self, part2=other)
        elif other == fire:
            return Lightning(part1=self, part2=other)
        elif other == ground:
            return Dust(part1=self, part2=other)

class Ground:

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if other == water:
            return Dirt(part1=self, part2=other)
        elif other == air:
            return Dust(part1=self, part2=other)
        elif other == fire:
            return Lava(part1=self, part2=other)

class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if other == water:
            return Steam(part1=self, part2=other)
        elif other == air:
            return Lightning(part1=self, part2=other)
        elif other == ground:
            return Lava(part1=self, part2=other)
class Steam:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + ' = Пар'

class Storm:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + ' = Шторм'
    
class Dirt:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + ' = Грязь'

class Lightning:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + ' = Молния'
    

class Dust:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + ' = Пыль'
    
class Lava:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + ' + ' + str(self.part2) + ' = Лава'


water = Water()
air = Air()
fire = Fire()
ground = Ground()

print("Список элементов: ")
all_elements = {'Вода' : water, 'Воздух' : air, 'Огонь' : fire, 'Земля' : ground}
for key, value in all_elements.items():
    print("{}".format(key))
print()


print('Введите два элемента в формате: эл1 + эл2')
while(1):
    element1, element2 = map(str, input().split(' + '))
    result = all_elements[element1] + all_elements[element2]
    print(result)
    print()

#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава



















# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
