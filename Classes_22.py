class Geom:
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2):
        print(f'{self.__class__}')
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Line(Geom):

    def __init__(self, x1, x2, y1, y2, fill=None):
        super().__init__(x1, x2, y1, y2)
        print('Line')
        self.fill = fill

    def draw(self):
        print('Рисуем линию')


class Rect(Geom):

    def __init__(self, x1, x2, y1, y2, fill=None):
        #super это ссылка на объект посредник, через который происходит выхов методов базового класса
        #инициализатор базового класса вызывактся самым первым, чтобы ничего не переписалось из базового класса
        #в дочерний
        super().__init__(x1, x2, y1, y2)
        print('Rect')
        self.fill = fill

    def draw(self):
        print('Рисуем прямоугольник')


l = Line(1, 2, 3, 4)
r = Rect(1, 2, 3, 4)
