"""
Data-classes
Они нужны чтобы более емко и проще определять классы с данными в них уже много определено и самому прописывать
заново не надо
"""

from dataclasses import dataclass, field
from pprint import pprint


class Thing:
    def __init__(self, name, w, price):
        self.name = name
        self.weight = w
        self.price = price

    def __repr__(self):
        return f'{self.__dict__}'


# Тут уже есть repr и init и еще всякое что показыват pprint
@dataclass
class ThingData:
    name: str
    weight: int
    peice: float
    dims: list = field(default_factory=list)  # field с параметром делает присвоение пустого списка вызовом фунции list


t = Thing('a', 100, 1024)
td = ThingData('a', 100, 1024)


#pprint(ThingData.__dict__)
pprint(Thing.__dict__)