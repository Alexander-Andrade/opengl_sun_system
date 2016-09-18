import math

from Shapes.Point import Point
from Shapes.Shape import Shape
import Animation

from Shapes.EllipsePainter import EllipsePainter


class Ellipse(Shape):
    
    def __init__(self, center=Point(), a=0.0, b=0.0, angle=0.0, rotate_point=None):
        self.center = center
        self.a = a
        self.b = b
        self.angle = math.radians(angle)
        self.rotate_point = rotate_point
        self.painter = EllipsePainter(self)

    def parametric(self, t):
        x = self.center.x + self.a*math.cos(t)
        y = self.center.y + self.b*math.sin(t)
        return Animation.rotate_around(self.rotate_point, Point(x, y), self.angle)



    def set_gravitycenter(self, grav_center):
        self.center = grav_center


# class MatEllipse(Shape):
#
#     def __init__(self, center=Point(), a=0.0, b=0.0, angle=0, n=50):
#         pass

