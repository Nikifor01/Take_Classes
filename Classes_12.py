class Cat:
    def __init__(self, name, *args):
        self.name = name

    def __repr__(self):
        #выводит служебную информацию
        return f'{self.__class__} : {self.name}'

    def __str__(self):
        #выводит служебную информацию
        return f'{self.name}'

    def __len__(self):
        return len(self.__coords)

c = Cat('asdsa')
print(c) # отработал str так как через принт, в консоле бы отработал repr

class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))

p = Point(1,2,-3,-4,5)
print(len(p))
print(abs(p))

'''
__srt__ для отображения информации об объекте класса для пользователя (print, str) 
__repr__ для отображения информации об объекте класса для разработчика (в режиме отладки) 
__len__ позволяет применить len к эземплярам класса
__abs__ позволяет применить abs к эземплярам класса
'''