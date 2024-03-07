class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):

    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius

    def __sub__(self, other):
        if self.radius == other.radius:
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Circle(self.x - other.x, self.y - other.y, abs(self.radius-other.radius))


a = Circle(1,2,3)
b = Circle(1,2,2)
c = Circle(3,4,3)

standard = a - b
negative = b - a
zero_radius = a - c

print(standard.__dict__)
print(negative.__dict__)
print(zero_radius.__dict__)
print(type(zero_radius))
