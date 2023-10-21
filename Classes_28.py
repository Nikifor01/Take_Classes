"""
Пользовательские метаклассы
"""


# def create_class(name, base, attr):
#     attr.update({'MAX': 100, 'MIN': 100})
#     return type(name, base, attr)


#Этот класс по сути добавляет то что в нём есть при вызове метода get_coords из экземпляра Point
class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX': 100, 'MIN': 100})
        return type.__new__(cls, name, base, attrs)

    # def __init__(cls, name, base, attrs):
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 100
    #     cls.MIN_COORD = 0


class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)


pt = Point()
print(pt.get_coords())