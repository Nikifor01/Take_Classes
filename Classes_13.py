'''
Методы описанные здсь делают возможным прибавлять вычитать умножать и тд сразу на экземпляр класса
'''

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds must be integers')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}'

    @classmethod
    def __get_formated(cls, t):
        return str(t).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError('')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)

    #Для перестановки слагаемых местами
    def __radd__(self, other):
        return self + other

    #Для сокращений типа += -= итд
    def __iadd__(self, other):
        pass

    def  __sub__(self, other):
        pass

    def  __mul__(self, other):
        pass
    
    def  __truediv__(self, other):
        pass

    def  __floordiv__(self, other):
        pass

    def  __mod__(self, other):
        pass



c2 = 300 + Clock(1200)
#c3 = Clock(2000)
#c4 = c2 + c3
print(c2.get_time())
