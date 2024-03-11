from math import pi as pi


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return pi * (self.r ** 2)

    def get_perimeter(self):
        return 2 * pi * self.r
