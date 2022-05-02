def my_func (x, y):
    """Функиция возведения в степень с использованием **"""
    return x**y
print(my_func(2.2, -1))

def my_func2 (x, y):
    """Функиция возведения в степень с использованием цикла"""
    if y == - 1:
       return 1 / x
    else:
        y = abs(y)
        while y > 1:
             global result
             result = x
             result = result * x
             y = y - 1
             return (1 / result)
print(my_func2(2.2, -2))