class Backpack:
    """ Рюкзак """

    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    def __add__(self, other):
        new_obj = Backpack()
        new_obj.content.extend(self.content)
        new_obj.content.extend(other.content)
        return new_obj


my_backpack = Backpack(gift='бутерброд')
son_backpack = Backpack(gift='банан')
new_backpack = my_backpack + son_backpack
print(new_backpack)