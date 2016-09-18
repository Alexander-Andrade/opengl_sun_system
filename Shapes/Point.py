from Shapes.Shape import Shape

from Shapes.PointPainter import PointPainter


class Point(Shape):
    
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.painter = PointPainter(self)

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y, self.z + point.z)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y, self.z - point.z)

    def __mul__(self, point):
        return Point(self.x * point.x, self.y * point.y, self.z * point.z)

    def __truediv__(self, point):
        return Point(self.x / point.x, self.y / point.y, self.z / point.z)

    def as_tuple(self):
        return self.x, self.y, self.z

    def set_gravitycenter(self, point):
        self.x, self.y, self.z = point.as_typle()
    
    def __repr__(self):
        return "Point(x:{}, y:{}, z:{})".format(self.x, self.y, self.z)
