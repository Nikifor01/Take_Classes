"""
Наследование классов это когда мы передаюм дочернему классу все атрибуты и методы родительского класса
полезная штука так можно расширять классы под спецефичные штуки, можно через определение общих вещей в
родительских классах сокращать код (Это больше не нужно делать отдельно в каждом классе, можно просто
унаследовать из родительского)
"""


class Geom:
    name = 'Geom'

    def set_coords(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    def draw(self):
        print('Рисование прямоугольника')


l = Line()
r = Rect()

l.set_coords(1, 2, 3, 4)
r.set_coords(4, 3, 2, 1)

print(l.__dict__)
print(r.__dict__)

#Пишет явлется ли класс подклассом, но работает только с самими классами, а не их экземплярами
print(issubclass(Line, Geom))

# эта же уже работате с экземплярами
print(isinstance(Geom, object))
print(isinstance(l, Geom))
print(isinstance(l, Line))

'''
class Line(Geom):
    def draw(self):
        print('Рисование линии')

    def set_coords(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Rect(Geom):
    def draw(self):
        print('Рисование линии')

    def set_coords(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
'''
