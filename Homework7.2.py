from abc import ABC, abstractmethod
class Clothes(ABC):
    @abstractmethod
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def __add__(self, other):
        return f'Общий расход ткани составляет {round(self.size/6.5 + 0.5 + other.height*2 + 0.3, 2)}'

class Coat(Clothes, ABC):
    def __init__(self, size, height):
        super().__init__(size, height)

    @property
    def size_coat(self):
        return f'Расход ткани на пальто составляет {round(self.size/6.5 + 0.5, 2)}'

class Suit(Clothes, ABC):
    def __init__(self, size, height):
        super().__init__(size, height)

    @property
    def height_suit(self):
        return f'Расход ткани на костюм составляет {round(self.height*2 + 0.3, 2)}'

a = Coat(42,160)
b = Suit(40, 150)
print(b.height_suit)
print(a.size_coat)
print(a+b)