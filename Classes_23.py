class Geom:
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2):
        print(f'{self.__class__}')
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        super().__init__(x1, x2, y1, y2)
        self.__fill = fill

    def get_coords(self):
        return (self.__x1, self.__y1)


r = Rect(0, 2, 4, 6)
print(r.__dict__)
#__ Таким образом к приватным атрибутам пристаёт тот префикс из класса которого атрибут был вызван
# {'_Geom__x1': 0, '_Geom__x2': 2, '_Geom__y1': 4, '_Geom__y2': 6, '_Rect__fill': None}

r.get_coords()
#__ ошибка приватные отрибуты могут находиться только в базовом классе

#_ эти уже можно из дочерних вызывать и извне, так как протектед ничего не запрещает


