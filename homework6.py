# Task 1
from time import sleep
class TrafficLight:
    __color = ['Красный!', 'Желтый!', 'Зеленый!']
    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается... \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1
TrafficLight = TrafficLight()
TrafficLight.running()

# Task 2
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
    def mass(self):
        return self._length * self._width
class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume
r = MassCount(25, 10000, 125)
print(r.mass())

# Task 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
a = Position('Карл', 'Маркс', 'экономист', 120000, 25000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

# Task 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} трогается'
    def stop(self):
        return f'{self.name} останавливается'
    def turn_right(self):
        return f'{self.name} поворачивает направо'
    def turn_left(self):
        return f'{self.name} поворачивает налево'
    def show_speed(self):
        return f'Текущая скорость {self.name}: {self.speed}'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость городского авто {self.name}: {self.speed}')
        if self.speed > 40:
            return f'Скорость {self.name} выше допустимой для городского авто!!!'
        else:
            return f'Скорость {self.name} допустима для городского авто.'
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость рабочего авто {self.name}: {self.speed}')
        if self.speed > 60:
            return f'Скорость {self.name} выше допустимой для рабочего авто!!!'
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f'{self.name} - это полицейский авто'
        else:
            return f'{self.name} - это НЕ полицейский авто'
lamborghini = SportCar(120, 'красный', 'Lamborghini', False)
hyundai = TownCar(30, 'серый', 'Hyundai', False)
lada = WorkCar(70, 'белый', 'Lada', True)
ford = PoliceCar(110, 'синий',  'Ford', True)
print(lada.turn_left())
print(f'Когда {hyundai.turn_right()}, {lamborghini.stop()}')
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'Цвет {lada.name} - {lada.color}')
print(f'{hyundai.name} - машина полиции? {hyundai.is_police}')
print(f'{lada.name} - машина полиции? {lada.is_police}')
print(lamborghini.show_speed())
print(hyundai.show_speed())
print(ford.police())
print(ford.show_speed())

# Task 5
class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки {self.title}'
class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой.'
class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом.'
class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером.'
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())