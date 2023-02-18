"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car():

    def __init__(pers, max_speed, color, name, is_police):
        pers.max_speed = max_speed
        pers.color = color
        pers.name = name
        pers.is_police = is_police
        print(f'Автомобиль {name}, цвет {color} выпущен')

    def show_speed(pers, speed):
        pers.speed = speed
        print(f'Скорость движения {pers.speed} км/ч')
        if pers.speed  > pers.max_speed and not pers.is_police:
            print('Внимание! Превышение допустимой скорости!')

    def go(pers):
        print(f'{pers.name} старт')

    def stop(pers):
        print(f'{pers.name} остановка')

    def turn(pers, direction):
        print(f'{pers.name} поворот {direction}')

class TownCar(Car):

    def __init__(pers, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Семейный автомобиль, седан')

    def show_speed(pers, speed):
        pers.speed = speed
        super().show_speed(pers.speed)


class SportCar(Car):

    def __init__(pers, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Спортивный автомобиль, седан')


class WorkCar(Car):

    def __init__(pers, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Служебный автомобиль, фургон')

    def show_speed(pers, speed):
        pers.speed = speed
        super().show_speed(pers.speed)

class PoliceCar(Car):
    def __init__(pers, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Полицейский автомобиль, седан')


my_family_car = TownCar(60, 'синий', 'Hyndai Accent', False)
my_family_car.go()
my_family_car.show_speed(40)
my_family_car.show_speed(50)
my_family_car.show_speed(60)
my_family_car.turn('направо')
my_family_car.turn('налево')
my_family_car.stop()
print()

my_work_car = WorkCar(60, 'белый', 'Mercedes-Benz Sprinter', False)
my_work_car.go()
my_work_car.show_speed(40)
my_work_car.stop()
print()

police_car = PoliceCar(0, 'белый', 'Ford Focus', True)
print()

sport_car = SportCar(60, 'красный', 'Porsche 911 GT3', False)
sport_car.go()
sport_car.show_speed(60)
sport_car.show_speed(70)
police_car.go()
police_car.show_speed(80)
police_car.turn('налево')
police_car.turn('направо')
police_car.stop()
sport_car.stop()