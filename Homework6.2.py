class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, weight_per_m, height):
        self.weight_per_m = weight_per_m / 0.01
        self.height= height / 100
        total_weight = (self._length * self._width * self.weight_per_m * self.height) / 1000
        return f'Нужно {total_weight} тонн асфальта'
a = Road(20, 5000)
print(a.weight(25, 5))