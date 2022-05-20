with open("persons.txt") as fp:
    my_dict = {}
    workers = []
    for line in fp:
        a = line.split()
        my_dict[a[0]] = float(a[1])
    for key, val in my_dict.items():
        if val <= 20000.00:
            workers.append(key)
print(f'Список сотрудников, чья з/п менее 20000: {workers}')
print(f'Средняя з/п всех сотрудников составляет: {round(sum(my_dict.values()) / len(my_dict), 2)}')
