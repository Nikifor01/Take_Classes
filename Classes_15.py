'''
хэши вычисляются только для неизменяемых объектов типа кортежей
и для одинаковызх объектов хэши всегда равны, но это не значит что для одинаковых хэшей объекты будут равны
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        #Вот при таком подходк ломается встроенная в python функция hash это надо лечить
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        #Вычисляем хэш уже от наших точек
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 2)

print(hash(p1), hash(p2), sep='\n')


