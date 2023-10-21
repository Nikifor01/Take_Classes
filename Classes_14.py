'''
Методы описанные здесь нужны для того чтобы можно было желать всякие сравнительные операции между экземплярами классов
'''

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds must be integers')
        self.seconds = seconds % self.__DAY

    @classmethod
    def __ver(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('')

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__ver(other)
        return self.seconds == sc

    def __ne__(self, other):
        sc = self.__ver(other)
        return self.seconds > sc

    def __lt__(self, other):
        sc = self.__ver(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.__ver(other)
        return self.seconds > sc

    def __le__(self, other):
        sc = self.__ver(other)
        return self.seconds <= sc

    def __ge__(self, other):
        sc = self.__ver(other)
        return self.seconds >= sc

c1 = Clock(2000)
c2 = Clock(2000)
print(c1 == c2)
print(c1 >= c2)
print(c1 < c2)
print(c1 != c2)