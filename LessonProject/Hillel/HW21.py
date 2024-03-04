import time


class Auto:

    def __init__(self, brand, age, mark, color='white', weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1


class Truck(Auto):

    def __init__(self, brand, age, mark, max_load, color='white', weight=3.5):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('!ATTENTION!')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color='white', weight=1.5):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'Max speed: {self.max_speed}')


truck_1 = Truck('SCANIA', '3', 'Mark1', '22')
truck_2 = Truck('VOLVO', 5, 'Mark3', 27, 'blue', 12)
print('\nTruck 1 motion test')
print(truck_1.__dict__)
truck_1.load()
truck_1.move()
truck_1.stop()
print('\nTruck 2 birthday test')
print(truck_2.__dict__)
truck_2.birthday()
print('Birthday was here')
print(truck_2.__dict__)
print('-' * 100)
print('Car_1 test')
car_1 = Car('Peugeot', 8, '208', 160)
print(car_1.__dict__)
car_1.move()
car_1.stop()
print('\nCar_2 test + birthday')
car_2 = Car('Audi', 10, 'A4', 200, weight=1.6)
print(car_2.__dict__)
car_2.move()
car_2.stop()
car_2.birthday()
print('Birthday was here')
print(car_2.__dict__)
