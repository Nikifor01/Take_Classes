class Calc:
    """
    Первая версия класса калькулятора, самая тупая, насколько возможно сделать её тупой
    """

    def __init__(self, x: [int, float] = 0, y: [int, float] = 0, z: [int, float] = 0):
        if type(x) in (int, float) and type(y) in (int, float) and type(z) in (int, float):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise ValueError('It must be int or float')

    @staticmethod
    def summ(x=0, y=0, z=0):
        return x + y + z

    def defi(self):
        return self.x - self.y - self.z

    @staticmethod
    def prod(x=0, y=0, z=0):
        return x * y * z


# c = Calc(3, 4, 8)
# print(c.summ(5.3, 8))
# print(c.defi())


class CalcOne:
    """
    Вторая версия класса уже лучше, но уже с возможностью вводить неограничеено количество аргументов, а так же в
    зависимости от того переданы ли в функцию парметры производить операцию либо над тем, что передано в экземпляр,
    либо над тем что передано в функцию
    """

    PI = 3.14

    def __init__(self, *args):
        if all(isinstance(arg, (int, float)) for arg in args):
            self.args = args
            self._pi = 3.14
        else:
            raise ValueError('It must be int or float')

    def sum(self, *args):
        if args:
            result = sum(args)
        else:
            result = sum(self.args)
        return result

    def defi(self, *args):
        if args:
            result = sum(args)
        else:
            result = sum(self.args)
        return result


c1 = CalcOne(2, 3, 4.4, 5)
print(c1.sum(2,3,4,5) * c1._pi)

