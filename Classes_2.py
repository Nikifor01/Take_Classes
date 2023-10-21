
class Point:

    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print('Вызвался перед тем как сборщик муссора удалил объект' + str(self))
    
    def prod(self):
        return self.x * self.y


p = Point(3, 5)
print(p.__dict__)
print(p.prod())

p.x = 2
p.y = 5
print(p.prod())

print(p.__dict__)
print(Point.__dict__)

Point.x = 12
Point.y = 13

print(p.__dict__)
print(Point.__dict__)


'''
__init__ это инициализатор, он делает так, что при создании нового экземпляра класса 
в нём уже будет то, что прописано в __init__

Таким образом, разница заключается в том, что метод `prod(self)` использует уже существующие 
значения `x` и `y`, тогда как метод `prod(self, x, y)` может использовать как существующие 
значения, так и значения, переданные явно при вызове метода.
'''