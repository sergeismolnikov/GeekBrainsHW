# 1



from itertools import cycle
from time import sleep

#сущее
class TrafficLight:
    # бытие делает сущее сущим
    __colors = {'red': 7, "yellow": 2, "green": 5}
    iterator_to_start = 0
    r_color = "red"
    y_color = 'yellow'
    g_color = "green"

    # метод бытия
    def running(self, iterations):
        perekluchator = cycle(self.__colors)
        start_color = 'blinking...'
        while iterations: #значение передается в метод извне
            current_color = next(perekluchator) #задаем переход по словарю цветов
            if TrafficLight.iterator_to_start == 0 and current_color == "red":
                print(start_color)
            elif TrafficLight.iterator_to_start == 1:
                print (f"current light is:{current_color}  "
                       f"you have to wait or walk through for: {TrafficLight.__colors[current_color]}  sec"
                       f"previous light was: blinking...  ")
            else:
                print(f"current light is:{current_color}  "
                      f"you have to wait or walk through for: {TrafficLight.__colors[current_color]}  "
                      f"previous light was:{start_color}  ")
            sleep(self.__colors[current_color])
            start_color = current_color
            iterations = iterations - 1
            TrafficLight.iterator_to_start +=1
print('input amount of the traffic light iterations please')
a = int(input())

traffic_light = TrafficLight()
traffic_light.running(a)

# 2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asph(self, mass, thickness):
        return self._length * self._width * mass * thickness

road = Road(20, 5000)

print(road.mass_asph(25, 5))


# 3
class Worker:

    def __init__(self, name, surname, position, income):
        self.w_name = name
        self.w_surname = surname
        self.w_position = position
        self._income = income

class Position (Worker):

    def get_full_name(self):
        return self.w_name + " " + self.w_surname

    def get_total_income(self):
        return self._income ["wage"] + self._income["bonus"]

w_income = {"wage": 11111111, "bonus": 2222222}

position = Position(name = "Sergei", surname= 'Smolnikov', position = "memechemist", income = w_income)
print(position.get_full_name())
print(position.get_total_income())


# 4
class cycle:
    def __init__(self, c):
        self._c = c
        self._index = -1

    def __next__(self):
        self._index += 1
        if self._index>=len(self._c):
            self._index = 0
        return self._c[self._index]

    def previous(self):
        self._index -= 1
        if self._index < 0:
            self._index = len(self._c)-1
        return self._c[self._index]

class Car:
    directions = {0: "North", 1: "East", 2:"South", 3:"West"}
    count = 0

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.car_speed = speed
        self.car_color = color
        self.car_name = name
        self.car_is_police = is_police
        self.stance = {"move": False}


    def go(self):
        self.stance["move"] = True
    def stop(self):
        self.stance["move"] = False
    def turn(self, direction):
        a = cycle(Car.directions)
        if direction not in ("left", "right"):
            raise ValueError("something wrong with your direction")
        elif direction == "left":
            self.count = a.previous()
        elif direction == "right":
            self.count = next(a)

    def show_speed(self):
        return {"speed": self.show_speed, "message":[]}
    def show_direction(self):
        return self.count

class PoliceCar (Car):
    pass
class SportCar (Car):
    pass

class CityCar(Car):
    sp_limit = 0
    def show_speed(self):
        sp_info = super().show_speed()
        if sp_info["speed"] > self.sp_limit:
            sp_info["message"].append("speed limit exceeded")
        return sp_info

class WorkCar(CityCar):
    sp_limit = 40
class TownCar(CityCar):
    sp_limit = 60


car = WorkCar(speed=200, color="red", name="mazda", is_police=False)

car.turn("right")
print(Car.count)
car.turn("right")
print(Car.count)
car.turn("right")
print(Car.count)
car.turn("right")

print(car.show_direction())
print(car.show_speed())


