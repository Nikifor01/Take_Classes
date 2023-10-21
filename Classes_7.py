class Attrs:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        #Работает когда происходит считываение атрибута класса через экземпляр
        print('smth')
        if item == 'x':
            raise ValueError("I don't think so")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        #Работает когда происходит присвоение какого-либо значения атрибуту
        ## два раз потомучто у нас x и y дважды сначала х потом у
        print('smth1')
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        #Работате тогда когда происходит обращение к несуществуещему методу из экземпляра класса
        return False

    def __delattr__(self, item):
        #Работает когда происходит удаление атрибута
        print('it was delt')
        object.__delattr__(self, item)

a = Attrs()
a.y
print(a.g)
del a.x
print(a.__dict__)