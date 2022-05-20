with open("my_text.txt", "w") as my_f:
    while True:
        a = input('Введите строку  или нажмите пробел для завершения') + '\n'
        if a ==' ' + '\n':
            break
        else:
            my_f.write(a)