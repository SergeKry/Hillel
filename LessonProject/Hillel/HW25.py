class Car:
    FUEL_TYPES = ['бензин', 'дизель', 'електрика', 'гібрид']
    COLORS = []
    NUMBERS_OF_CARS = 0

    @staticmethod
    def is_valid_fuel_type(fuel, available_types):
        if fuel.lower() in available_types:
            return fuel
        else:
            return available_types[0]

    def __init__(self, model, year, color, fuel_type):
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = Car.is_valid_fuel_type(fuel_type, Car.FUEL_TYPES)
        Car.NUMBERS_OF_CARS += 1
        if self.color not in Car.COLORS:
            Car.COLORS.append(color)
        self.number = Car.NUMBERS_OF_CARS

    @property
    def numbers(self):
        return ' of '.join([str(self.number), str(Car.NUMBERS_OF_CARS)])

    def __repr__(self):
        return f'{self.model}-{self.year}-{self.fuel_type}-{self.color}'

    @classmethod
    def get_used_colors(cls):
        return len(cls.COLORS)

    @classmethod
    def get_number_of_cars(cls):
        return cls.NUMBERS_OF_CARS


car_1 = Car('Zaz', 1979, 'black', 'дизель')
car_2 = Car('BMW', 2000, 'red', 'бензин')
car_3 = Car('VOLVO', 2012, 'black', 'електрикаcccc')
car_4 = Car('Mersedes', 2012, 'black', 'гібрид')
print('COLORS:', Car.get_used_colors())
print('NUMBER_OF_CARS:', Car.get_number_of_cars())
for item in (car_1, car_2, car_3, car_4):
    print('item:', item)
    print('numbers:', item.numbers)
