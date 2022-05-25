class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus): #если удалить 9 и 10 стр, без них тоже работает
        super().__init__(name, surname, position, wage, bonus)
    def get_full_mame(self):
        return f'Сотрудник {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход {self.name} {self.surname} составляет {self._income["wage"] + self._income["bonus"]}'

b = Position('Вася', 'Пупкин', 'менеджер', 9000, 7000)
c = Position('Петя', 'Петров', 'оператор', 8000, 79000)
print(b.get_full_mame())
print(c.get_total_income())
print(b.name, b.surname)
print(f'Должность {c.position}а занимает {c.surname}')