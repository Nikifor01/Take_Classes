
class Incaps:
    '''
    public – def func() обычный метод доступная откуда угодно
    protected – def _func() - можем обращаться только внутри класса и дочерних классах
    private – def __func() - можем обращаться только внутри текущего класса
    то же самое справедливо и для атрибутов
    '''

    def __init__(self, a=0, b=0, e=0, f=0, x=0, y=0):

        self.a = self.b = self.e = self.f = self.x = self.y = 0

        if self.__valid_cord(x) and self.__valid_cord(y):
            self.a = a
            self.b = b

            self._e = e
            self._f = f

            self.__x = x
            self.__y = y

    @classmethod
    def __valid_cord(cls, arg):
        return type(arg) in (int, float)

    def set_coord(self, x, y):
        if self.__valid_cord(x) and self.__valid_cord(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Not a Number")

    def get_coord(self):
        return self.__x * self.__y


i1 = Incaps(a=2, b=3)
print(i1.a) #к нему мы можем обратиться из экзепляра

i2 = Incaps(e=2, f=3)
print(i2._e) #к нему мы можем обратиться из экзепляра но не нужно, испортите класс

i3 = Incaps(x=2, y=3)
#print(i3.__x) #к нему мы уже обратиться напрямую не можем, совсем скрытый парень, но можем внутри класса совершенно спокойно

#Вот тут начинается занимательная история про геттеры и сеттеры, сеттеры устанавливают значения в закрытые переменные
#чтобы не сломать класс, а геттеры вытаскивают их для нас чтобы мы могли в дальнейшем использовать результат
i3.set_coord(100, 6)
print(i3.get_coord())

##i3.set_coord('as', 6)
##print(i3.get_coord())

#Вот отсюда можно и к приватному обратиться, но это крайне не рекомендуется, только на ваш страх и риск
print(dir(i3))