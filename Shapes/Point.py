from Shapes.Shape import Shape

from Shapes.PointPainter import PointPainter
import numpy as np

class Point(Shape):
    
    def __init__(self, x=0.0, y=0.0, z=0.0, has_painter=False):
        self.x = x
        self.y = y
        self.z = z
        if has_painter:
            self.painter = PointPainter(self)

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y, self.z + point.z)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y, self.z - point.z)

    def __mul__(self, point):
        return Point(self.x * point.x, self.y * point.y, self.z * point.z)

    def __truediv__(self, point):
        return Point(self.x / point.x, self.y / point.y, self.z / point.z)

    def __eq__(self, point):
        return True if self.x == point.x and self.y == point.y else False

    def __ne__(self, other):
        return not self.__eq__(other)

    def as_tuple(self):
        return self.x, self.y, self.z

    def as_array(self):
        return np.array([self.x, self.y, self.z])

    @staticmethod
    def from_tuple(t):
        return Point(t[0], t[1], t[2])

    @staticmethod
    def from_array(arr):
        return Point(arr[0], arr[1], arr[2])

    def set_gravitycenter(self, point):
        self.x, self.y, self.z = point.as_typle()

    def gravity_center(self):
        return self

    def __repr__(self):
        return "Point(x:{}, y:{}, z:{})".format(self.x, self.y, self.z)
