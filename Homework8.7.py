class Complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a +other.a} + {(self.b + other.b)}i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} + {(self.b * other.a + other.b * self.a)}i'

c_n = Complex_number(5, 6)
c_n2 = Complex_number(3, 3)
print(c_n + c_n2)
print(c_n * c_n2)