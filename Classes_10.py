'''
дескриптор находится в отдельном классе, весь интерфейс взаимодействия с атрибутами там, в независимости от их колва
owner – Point3D ссылка
name – имя которому присваивается экземпляр класса
instance –
value –

как только мы создаём экземпляр класса integer срабатывает метод __set_name в резултате внутри x (например)хранится имя
атрибута
далее мы создаём экземпляр Point3D при создание вызывается инит в нём идёт обращение к экземплярам x, y, z класса Integer
и присваивается переданное в экземпляр Point3D значения
'''

class Integer:
    def __set_name(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def coord(self):
        return self.x, self.y, self.z

    @coord.setter
    def coord(self, *arg):
        self.x, self.y, self.z = arg


p3 = Point3D(3, 5, 6)
print(p3.__dict__)

'''
Здесь мы делаем так чтобы не нужно было для каждого атрибута отдельный геттер и сеттер
КАКАЯ-ТО СЛОЖНАЯ ШТУКА
'''