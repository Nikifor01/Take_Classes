'''
__call__ вызывается тогда когда мы вызываем класс определяя его экземпляр (когда мы пишем скобки и сохраняем это в переменную)
нужно чтобы экземпляр класса тоже смог стать вызываемым (callable)

вместо замыкания функции можно реализовывать класс StripChars
'''

class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('sdf')

        return args[0].strip(self.__chars)

s1 = StripChars("?!:; ")
res1 = s1("!!!Nkifor;;;")
print(res1)



class Functors:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print('__call__')
        self.__counter += step
        return self.__counter



c = Functors()
c(1)
c(2)
c(3)

res = c(5)

print(res)