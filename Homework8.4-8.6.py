class Warehouse:
    __storage = []
    _nomenclature = {}

    def receiving(self, position):
        if not isinstance(position, OfficeEquipment):
            raise Exception('Эта позиция не является оргтехникой')
        self.__storage.append(position)
        h = input(f'Сколько единиц {str(position)} отдаете на склад?')
        if self._nomenclature.get(position.name):
            if not h.isdigit():
                raise ValueError('Вы ввели не числа')
            else:
                self._nomenclature[position.name] += int(h)
        else:
            self._nomenclature.setdefault(position.name,int(h))

    @classmethod
    def extract(cls, position, direction):
        if position in cls.__storage:
            cls.__storage.remove(position)
            cls._nomenclature[position.name] -= 1
            return f'{position} передан в департамент {direction}'
        else:
            return f'Позиция "{position}" отсутствует на складе'

class OfficeEquipment:
    def __init__(self, name, color, brand, model):
        self.name = name
        self.color = color
        self.brand = brand
        self.model = model
    def __str__(self):
        return f'{self.name} {self.brand}'

class Printer(OfficeEquipment):
    def __init__(self, color, brand, model, printer_type, colorful):
        super().__init__('Принтер', color, brand, model)
        self.printer_type = printer_type
        self.colorful = colorful

class Scanner(OfficeEquipment):
    def __init__(self, color, brand, model, wireless):
        super().__init__('Сканнер', color, brand, model)
        self.wireless = wireless

class Xerox(OfficeEquipment):
    def __init__(self, color, brand, model, colorful):
        super().__init__('Ксерокс', color, brand, model)
        self.colorful = colorful


a = Printer('white', 'hp', '360', 'laser', True)
b = Printer('grey', 'canon', '690', 'jet', False)
c = Scanner('black', 'sony', '6790', False)
d = Xerox('white', 'samsung', '8900j', True)
e = Xerox('grey', 'hp', '7600j', False)
f = Printer('grey', 'epson', '0089', 'jet', True)

w = Warehouse()

w.receiving(a)
w.receiving(b)
w.receiving(c)
w.receiving(d)
w.receiving(e)
w.receiving(f)
print(w._nomenclature)
print(w.extract(b, 'Маркетинг'))
print(w._nomenclature)
print(w.extract(b, 'Финансовый отдел'))
print(w.extract(d, 'Юр отдел'))
print(w._nomenclature)



