'''
Правдивость класса это когда явно или неявно к объекту применяется функция __bool__()
она всегда возвращает true для всех объектов пользовательского класса

хэши разные
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x * self.x + self.y * self.y

    #Теперь при вызове бул будет происходить то что написано здесь делает экземпляры с равными хэшами
    #я так понял
    def __bool__(self):
        return self.x == self.y

p = Point(3, 4)
print(len(p))
print(bool(p))

p1 = Point(0, 0)
print(len(p1))
print(bool(p1))