import math
from dmg_generator.map_object import MapObject


class Side(MapObject):
    def __init__(self, length):
        self.length = length


class Room(MapObject):
    def __init__(self):
        for s in self.sides:
            s.connect(self)


class Rectangle(Room):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.sides = [Side(length), Side(width), Side(length), Side(width)]
        super().__init__()

    def rotate(self):
        self.length, self.width = self.width, self.length
        side = self.sides.pop()
        self.sides.insert(0, side)

    @property
    def short_sides(self):
        short = min(self.length, self.width)
        return [s for s in self.sides if s.length == short]

    @property
    def long_sides(self):
        long_ = max(self.length, self.width)
        return [s for s in self.sides if s.length == long_]


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)


class Circle(Square):
    def __init__(self, diameter):
        side = (diameter * math.pi) / 4.0
        super().__init__(side)
        self.diameter = diameter
