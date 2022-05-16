from functools import reduce

def func (a, b):
    result = a * b
    return result

Total = reduce(func, ([i for i in range(100, 1001) if i % 2 == 0]))

print(Total)