class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки инструментом {self.title}'

class Pencil(Stationery):
    def draw(self):
        return f'Вы рисуете инструментом {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'Выделение инструментом {self.title}'

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
s = Stationery('Канцелярка')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
print(s.draw())