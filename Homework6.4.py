class Car:
    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return f'Машина {self.name} поехала'
    def stop(self):
        return f'Машина {self.name} остановилась'
    def turn(self, direction):
        return f'Машина {self.name} повернула {direction}'
    def show_speed(self):
        return f'Машина {self.name} едет со скоростью {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return f'Вы превышаете скорость на {self.speed - 60} км/ч'
        else:
            return f'Машина {self.name} едет со скоростью {self.speed}'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превышаете скорость на {self.speed - 40} км/ч'
        else:
            return f'Машина {self.name} едет со скоростью {self.speed}'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


toyota = PoliceCar(50, 'red', 'Toyota')
audi = TownCar(90, 'black', 'Audi')
mercedes = WorkCar(120, 'grey', 'Mercedes')
gtr = SportCar(200, 'white', 'Nissan GTR')
print(toyota.is_police)
print(audi.name)
print(mercedes.color)
print(audi.show_speed())
print(gtr.show_speed())
print(f'{toyota.go()}, а {mercedes.stop()}, потому что {gtr.turn("налево")}')
print(mercedes.show_speed())