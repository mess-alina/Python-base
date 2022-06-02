class MyZerroDevision(Exception):
    def __init__(self, txt):
        self.txt = txt

ask = [i for i in input('Введите два числа через запятую').split(',')]

try:
    if int(ask[1]) == 0:
        raise MyZerroDevision("Делить на ноль нельзя")
    else:
        result = int(ask[0]) / int(ask[1])
        print(round(result, 1))
except ValueError:
    print('Вы ввели не числа')
except IndexError:
    print('Вы ввели недопустимые символы')
except MyZerroDevision as err:
    print(err)


