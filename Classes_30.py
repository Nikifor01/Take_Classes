from dataclasses import dataclass, field


class Vector:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5


@dataclass
class V3D:
    x: int = field(repr=False)  # удаляет из отображения в консоли (из магического repr)
    y: int
    z: int = field(compare=False)  # исключает из сравнения
    length: float = field(init=False)  # говорит о том, что не слудует добавлять в параметры инициализатора

    # Вызывается в классах с декораторм dataclass в конце работы такого класса
    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
print(v)
print(v.__dict__)
