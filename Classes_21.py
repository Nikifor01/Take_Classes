class Geom:
    name = 'Geom'

    def __init__(self):
        print('Рисуем')


class Line(Geom):
    # Вот тут происходит переопределение так как ре ищет функцию draw снизу вверхБ впервые он сталкивается тут
    # а не в родительском работает и с инитами и всем всем всем

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self):
        print('Рисуем линию')


class Rect(Geom):
    # Вот тут происходит переопределение так как ре ищет функцию draw снизу вверхБ впервые он сталкивается тут
    # а не в родительском работает и с инитами и всем всем всем

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self):
        print('Рисуем прямоугольник')


l = Line(1, 2, 3, 4)
