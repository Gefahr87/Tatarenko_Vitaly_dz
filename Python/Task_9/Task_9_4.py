'''
Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'
    def stop(self):
        return f'Машина {self.name} остановилась'
    def turn_duraction(self, duration):
        return f'Машина {self.name} повернула по направлению {duration}'
    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} составляет {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        return f'Превышение скорости по машине {self.name} {self.speed}' if self.speed > 60\
            else f'Скорость по машине {self.name} в норме'

class SportCar(Car):
    pass

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        return f'Превышение скорости по машине {self.name} {self.speed}' if self.speed > 40\
            else f'Скорость по машине {self.name} в норме'

class PoliceCar(Car):
    pass

victoria_car = PoliceCar(160, 'Black', '2685 Minnesota', True)
print(f'Машина цвета {victoria_car.color}.', victoria_car.show_speed())
lamba_car = SportCar(100, 'Red', 'Средство № 5', False)
print(f'Машина цвета {lamba_car.color}.', lamba_car.show_speed())
andry_car = TownCar(61, 'White', 'Полёт', False)
print(f'Машина цвета {andry_car.color}.', andry_car.show_speed())
yndx_car = WorkCar(40, 'Yellow', 'Cредство № 5', False)
print(f'Машина цвета {yndx_car.color}.', yndx_car.show_speed())

