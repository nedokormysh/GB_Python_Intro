####1
print("Task 1: Traffic Light \n---------\n")

import time

class TrafficLight:

    __color = ['red', 'yellow', 'green']

    def running(self):

        li_time = [7, 2, 3]

        j = 0
        while j < 3:
            for i in range(0, 3):
                print("Color of traffic light is",TrafficLight.__color[i])
                time.sleep(li_time[i])
            j += 1

a = TrafficLight()
a.running()



#####2

line = "=" * 150
print(line)
print("Task 2: Asphalt  \n---------\n")
try:
    length, width, depth = map(int, input('Enter numbers: Length, Width, Depth with spaces:').split())
except ValueError:
    print('Enter integers')
# except NameError:
#     print('Enter 3 numbers')

class Road():
    # _length = 20
    # _width = 5000

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def how_much_asphalt(self, _depth = 0.05):
        mass_to_cover_one_sq_meter = 25
        return self._length * self._width * (_depth/100) * mass_to_cover_one_sq_meter


a = Road(length, width)
print(a.how_much_asphalt(depth))

##### 3

line = "=" * 150
print(line)
print("Task 3: Workers  \n---------\n")

class Worker():
    # name, surname, position, income, {"wage": wage, "bonus": bonus};
    def __init__(self, name, surname, position,  wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.income = {"wage": self.wage, "bonus": self.bonus}

class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name
    def get_total_income(self):
        income = self.income.get('wage') + self.income.get('bonus')
        return income

name = 'Il'
surname = 'Ber'
position = 'engineer'
bonus = 5000
wage = 100000
a = Position(name, surname, position, wage, bonus)
# a = Worker

print(dir(Worker))
print(dir(Position))
print("Full name is",a.get_full_name())
print(a.position)
print("Total income of", a.get_full_name(),'is',a.get_total_income())


####4

line = "=" * 150
print(line)
print("Task 4: Cars  \n---------\n")

class Car:
    speed = 60
    default_color = 'green'
    default_name = 'noname'
    isPolice = False

    def __init__(self, speed, color, name, isPolice):
        self.speed = speed
        self.color = color
        self.name = name
        self.isPolice = isPolice

    def go(self):
        return f'The {self.color} {self.name} is going'

    def stop(self):
        return f'The {self.color} {self.name} stopped'

    def turn_direction(self):
        return f'The {self.color} {self.name} changed direction to the left'

    def show_speed(self):
        return f'The {self.color} {self.name} has {self.speed}km/h'

class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            return (f'The {self.color} {self.name} has {self.speed}km/h. The speed of car is overspeed. '
                    f'It is over 60')
        else:
            return f'{Car.show_speed(self)}. It is ok for car in town'

class SportCar(Car):
    def is_Porsche(self):
        if self.name != 'Porsche':
            return "It's not a sport car"

class WorkCar(Car):
    def show_speed(self):

        if self.speed > 40:
            return (f'The {self.color} {self.name} has {self.speed}km/h. The speed of car is overspeed. '
                    f'It is over 40')
        else:
            return f'The {self.color} {self.name} has {self.speed}km/h. It is ok for car for work'

class PoliceCar(Car):
    def __init__(self, speed, color, name, isPolice, music):
        super().__init__(speed, color, name, isPolice)
        self.music = music

Audi = SportCar(100, 'red', 'Audi', True)
Renault = WorkCar(50, 'blue','Renault', False)
Lada = PoliceCar(150, 'yellow', 'Lada', True, True)
Volkswagen = TownCar(60, 'grey', 'Volkswagen', False)

print(Renault.show_speed())
print(f'Will the {Lada.name} follow the intruder? {Lada.isPolice}. So it is a chase')
print(Lada.show_speed())
print(f'Is {Lada.name} a police car? {Lada.isPolice}')
print(f'Is {Lada.name} has music signal', Lada.music)
print(f'Where did {Audi.name} has gone? {Audi.turn_direction()}')
print(f'Does {Audi.name} is real sport car?', Audi.is_Porsche())
print(Volkswagen.show_speed())
print(Audi.show_speed())
print(Audi.stop(), f'by {Lada.name}')

#######5

line = "=" * 150
print(line)
print("Task 5: Drawing  \n---------\n")

class Stationery:
    # title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'This is {self.title}')

class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'This is {self.title}')

class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'This is {self.title}')

a = Pen('pen')
b = Pencil('pencil')
c = Handle('handle')

a.draw()
b.draw()
c.draw()