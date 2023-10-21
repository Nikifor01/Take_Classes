from dataclasses import dataclass, field, InitVar


class Vector:
    def __init__(self, x: int, y: int, z: int, calc_len = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5


@dataclass
class V3D:
    x: int = field(repr=False)  # удаляет из отображения в консоли (из магического repr)
    y: int
    z: int = field(compare=False)  # исключает из сравнения
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)  # говорит о том, что не слудует добавлять в параметры инициализатора

    # Вызывается в классах с декораторм dataclass в конце работы такого класса
    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
print(v)
print(v.__dict__)
