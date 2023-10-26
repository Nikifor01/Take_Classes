"""
__slots__ это штука которая показывает какие имена для локальных свойств класса и экземпляра допустимы
а так же очень нефигово экономит память
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p2d = Point2D(2, 5)
print(p2d.x)
p2d.x = 4
print(p2d.x)
# Вот тут появится ошибка потому что __slots__ не даёт создать локальные атрибуты с именами которые в нём не определены
p2d.z = 0

# Nothing
print(p2d.__dict__)
# Ещё __slots__ не созадёт коллекцию dict, её теперь просто нет это экономит память и время испольнения
# а вообще не только этим он экономит, крутая штука, но пока непонятно как так получается
