class Vector(list):
    def __str__(self):
        return "".join(map(str, self))


# Мы расширили класс лист дочерним классом Vector и теперь список возвращается строкой, а не списком, как обычно
v = Vector([1, 2, 3, 4, 5])
print(v)
