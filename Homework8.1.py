class Date:
    def __init__(self, ask):
        self.ask = ask

    @classmethod
    def integer(cls, ask):
        a = [int(i) for i in ask.split('-')]
        return f' Дата: {a[0]}-{a[1]}-{a[2]}'

    @staticmethod
    def validation(ask):
        my_list = [int(i) for i in ask.split('-')]
        if 1 <= my_list[0] <= 31:
            if 1 <= my_list[1] <= 12:
                if 1 <= my_list[2]:
                    return f'Дата введена корректно'
                else:
                    return f'Год введен не корректно'
            else:
                return f'Месяц введен не корректно'
        else:
            return f'Дата введена некорректно'



a =Date('13-05-2022')
print(a.integer('13-05-2022'))
print(Date.integer('01-09-2001'))
print(Date.validation('13-05-2022'))
print(Date.validation('43-05-2022'))
print(Date.validation('16-13-2022'))
print(Date.validation('16-10-0'))
