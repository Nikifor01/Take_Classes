# Вот так не надо потому что нет полиморфизма, то есть у нас два почти одинаковых класса
# c одинаковыми геттерами, так почему бы нам не сделать так, чтобы метод который вызывает эти геттеры был
# одинаков для каждого из похожих классов и потом мы могли циклом вызывать эти метод для разных экзкмпляров
# тогда у нас получится полиморфизм
"""
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_rect_pr(self):
        return 2 * (self.a + self.b)

class Squa:
    def __init__(self, a):
        self.a = a

    def get_rect_pr(self):
        return 2 ** self.a
"""


# Вот так надо
class Geom:
    def get_pr(self):
        return -1


class Rect(Geom):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_pr(self):
        return 2 * (self.a + self.b)


class Squa(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 2 ** self.a


class Tria(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 3 ** self.a

geom = [Tria(5), Squa(3), Rect(7, 6)]

for i in geom:
    print(i.get_pr())