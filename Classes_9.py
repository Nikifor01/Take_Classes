from string import ascii_letters

class Person:
    S_RUS = 'абвгдеёжзиклмнопрстуфхцчшщьыъэюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weigth):
        self.ver_fio(fio)
        self.ver_old(old)
        self.ver_weigth(ps)
        self.ver_pas(weigth)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weigth = weigth

    @classmethod
    def ver_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("FIO must be string")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("NOOOOOO")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for i in s:
            if len(s) < 1:
                raise TypeError("There is nothing")
            if len(s.strip(letters)) != 0:
                raise TypeError("There is numbers or so,ething")

    @classmethod
    def ver_old(cls, old):
        if type(old) not in (int, float):
            raise TypeError("It must be number")

    @classmethod
    def ver_weigth(cls, weigth):
        if type(weigth) not in (int, float):
            raise TypeError("It must be number")

    @classmethod
    def ver_pas(cls, ps):
        if type(ps) != str:
            raise TypeError("It must be string")

        s = ps.split()
        if len(s) < 2 or len(s[0]) != 4 or len(s[0]) != 6:
            raise TypeError("It must be two")

        for p in s:
            if not p.isdigit():
                raise TypeError("It must be number")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @property
    def weigth(self):
        return self.__weigth

    @weigth.setter
    def weigth(self, weigth):
        self.__weigth = weigth

    @property
    def ps(self):
        return self.__old

    @ps.setter
    def ps(self, ps):
        self.__passport = ps

#Вот так работает property декоратор лднако приходится писать кучу всего
#для того чтобы этого избежать существует дескриптор рассмотренный в следующем классе