class Point:
    Min = 0
    Max = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def prod(self):
       if Min <= self.x <= Max:
           return 'brrrr'

'''
здесь мораль таковаБ что мы не можем из метода обратиться к атрибутам класса не указав класс или ссылку на первый
попавшийся через self
'''

#Так нельзя
p = Point()
##print(p.prod())


#А вот так можно
class Point:
    Min = 0
    Max = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def prod(self):
       if self.Min <= self.x <= self.Max:
           return 'brrrr'

p1 = Point()
print(p1.prod())

#тут в последнем методе присвоится занчение экземпляру, это ошибка мы этого не хотели
class Point:
    Min = 0
    Max = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def prod(self):
       if self.Min <= self.x <= self.Max:
           return 'brrrr'

    def set_it(self, min):
        self.Min = min
        #вот только прикол в том тут что в самом классе ничего не изменится, изменится, а точнее появится только
        #в экземпляре, так как self это ссылка экземпляра

p2 = Point()
p2.set_it(4)
print(Point.__dict__)
print(p2.__dict__) #что хорошо видно в dict

# Правильно чтобы изменитб именно то что внутри самого класса делается через методы в этом классе
class Point:
    Min = 0
    Max = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def prod(self):
       if self.Min <= self.x <= self.Max:
           return 'brrrr'

    @classmethod
    def set_it(cls, min):
        cls.Min = min
        #вот только прикол в том тут что в самом классе ничего не изменится, изменится, а точнее появится только
        #в экземпляре, так как self это ссылка экземпляра

p3 = Point()
p3.set_it(4)
print(Point.__dict__)
print(p3.__dict__) #теперь всё поменялось, так как мы воздействовали на сами атрибуты класса через cls



