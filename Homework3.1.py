def funcDevision(a, b):
    try:
        Result = a / b
        return Result
    except: ZeroDivisionError
    return 'Ошибка - на ноль делить нельзя'
while True:
    ask = input('Введите два числа через пробел, для выхода нажмите "q"').split()
    if ask == ['q']:
        break
    else:
        askList = list(map(int, ask))
        print(funcDevision(askList[0], askList[1]))


