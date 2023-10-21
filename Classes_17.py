'''
Методы которые позволяют работать с переменными как со словарями и списками с помощью экземпляров класса
'''

class Point:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    #Даёт обращаться к списку от имени экземпялра
    def __getitem__(self, item):
        return self.marks[item]

    #Даёт возможность присвоить новое значение по индексу
    def __setitem__(self, key, value):
        self.marks[key] = value

    #Даёт вохможгность удалить элемент из списка
    def __delitem__(self, key):
        del self.marks[key]


s1 = Point('Sergey', [2,3,4,5,4,5,3,3,3])
print(s1[0])
s1[2] = 1
print(s1.marks)