proceeds = int(input('Введите сумму выручки'))
expenses = int(input('Введите сумму издержек'))
profit = proceeds - expenses
if proceeds > expenses:
    print('Финансовый результат положительный. Рентабельность выручки составляет', profit/proceeds)
    if proceeds > expenses:
        personal = int(input('Введите количество сотрудников'))
        print('Прибыль фирмы на сотрудника =', profit / personal)
else:
    print('Финансовый результат отрицательный')


