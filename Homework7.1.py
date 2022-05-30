class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return str('\n'.join(str(i) for i in self.matrix_list))

    def __add__(self, other):
        c = [[None for __ in range(len(self.matrix_list[0]))] for __ in range(len(self.matrix_list))]

        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[0])):
                c[i][j] = self.matrix_list[i][j] + other.matrix_list[i][j]
        return str('\n'.join(str(k) for k in c))

a = Matrix([[1, 2, 3], [4, 3, 4]])
b = Matrix([[3, 3, 2], [2, 5, 6]])

print(f'Экземпляр класса "Матрица" \n{b}')
print(f'Результат сложения двух экземпляров класса "Матрица": \n{a+b}')