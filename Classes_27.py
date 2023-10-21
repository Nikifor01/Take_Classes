"""
Метаклассы это что создаёт классы объекты

объекты(False, 'Hello', 123, 56.67) ==> объектыб классы (bool, str, int, float) ==> метакласс type(name, bases, dct)

Все стандартные классы пораждены метаклассом type

"""

print(type(int))  # ==> class 'type'

# Тут мы сосздаём класс иным образом

A = type('Point', (), {'MAX': 100, 'MIN': 100})

pt = A()
print(pt.MAX)


class B1:
    pass


class B2:
    pass


B = type('Vec', (B1, B2), {'MAX': 100, 'MIN': 0})

print(B.__mro__)