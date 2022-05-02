sum_result = 0
e = False
while e == False: # Тут я не поняла почему, но с True не работал break. Поясните почему, пожалуйста
    ask = input('Введите числа через пробел. Для выхода нажмите "q"').split()
    result = 0
    for i in ask:
        if i == 'q':
            ask.remove(i)
            result = result + sum(list(map(int, ask))) # Это для усл, что символ введен после чисел, и их нужно добавить к рез-ту
            e = True
            break
            print(sum_result)

    result = result + sum(list(map(int, ask))) # Когда тут было else программа игнорировала условие if. Я долго мучалась
    sum_result = sum_result + result
    print(sum_result)


