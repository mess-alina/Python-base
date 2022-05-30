class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def __str__(self):
        return f'Ячеек в клетке после операции: {self.amount}'

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        return Cell(self.amount - other.amount) if self.amount - other.amount > 0 else f'Разность клеток меньше нуля'

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(int(self.amount / other.amount))

    def make_order(self, cell_in_row):
        row = f'{"*"* cell_in_row}\\n' * round(self.amount / cell_in_row)
        return f'{row + str("*" * round(self.amount % cell_in_row))}'

a = Cell(2)
b = Cell(18)
n = Cell(3)
print(a+b)
print(a-b)
print(b-n)
print(a*b)
print(b/n)
print(b.make_order(5))
