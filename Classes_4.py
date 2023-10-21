'''
@classmethod работает исключительно с атрибутами класса (не экземпляра)
@staticmethod просто тупо функция в отрыве от классов и его экземпляров
'''

class Vector:

    MIN = 0
    MAX = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN <= arg <= cls.MAX

    def __init__(self, x=0, y=0, z=0):
        self.x = self.y = self.z = 0

        if self.validate(x) and self.validate(y) and self.validate(z):
            self.x = x
            self.y = y
            self.z = z

        print(self.prod(7, 8))

    def get_coord(self):
        return (self.x, self.y, self.z)

    @staticmethod
    def prod(x, y):
        return x * y

v = Vector(101,23,4)
print(v.get_coord()) 

v1 = Vector(90,23,4)
print(v1.get_coord())

v2 = Vector()
print(v2.prod(2, 5))

'''
Обычные методы работают с атрибутами экземпляра класса и с атрибутами самого класса
@classmethod работают только с атрибутами класса
@staticmethod работают с чем угодно просто функция как в программе без классов если такие бывают
'''