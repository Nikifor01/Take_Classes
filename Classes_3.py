
class Point:

    def __new__(cls, *args, **kwargs):
        print('вызвался new' + str(cls))

    def __init__(self, x=0 , y=0):
        self.x = x
        self.y = y


#Заметим что вызвался только new, значит экземпляр не создан
p = Point()
# он возвращает None
print(p)
#Так произошло потому что new должен возвращать адрес нового объекта, а тут этого не происходит
# СОЗДАДИМ КЛАСС ПОДРУГОМУ ЧТОБЫ ЭКЗЕМПЛЯР СОЗДАВАЛСЯ

class Vector:

    def __new__(cls, *args, **kwargs):
        print('вызвался new' + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print('вызвался init' + str(self))
        self.x = x
        self.y = y

v = Vector()
# он возвращает None
print(v)

'''
ВАЖНО ЗАПОМНИТЬ ЧТО:
cls ссылается на текущий класс то есть тупо на класс Point и его атрибуты (не локальные)
self в свою очередь ссылается на экземпляр класса и всё что в нём есть (локальное)

метод new вызывается при создании объекта, а метод init при инициализации экземпляра этого объекта

есть базовый класс object, все создаваемые нами классы от него наследуются
вызывая super() мы получем ссылку на этот базовый класс и в нём уже вызываем new и он уже и запускает процесс
создани яэкземпляра класса
'''

#Пример паттерна Singleton – предполагает что в программе должен существовать только один экземпляр этого класса

class SingleTon:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance == super().__new__(cls)
        return cls.__instance

    def __init__(self, x=0, y=1, z=2):
        self.x = x
        self.y = y
        self.z = z

    def __del__(self):
        self.__instance = None

    def connect(self):
        print(f'{self.x}, {self.y}, {self.z}')


s = SingleTon()
s1 = SingleTon()

print(id(s), id(s1))