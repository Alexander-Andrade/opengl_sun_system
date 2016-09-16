from Shape import Shape
from Point import Point
import math
from EllipsePainter import EllipsePainter

class Ellipse(Shape):
    
    def __init__(self, center=Point(), a=0.0, b=0.0):
        self.center = center
        self.a = a
        self.b = b
        self.painter = EllipsePainter(self)

    def parametric(self, t):
        return Point(self.center.x + self.a*math.cos(t), self.center.y + self.b*math.sin(t))

    def set_gravitycenter(self, grav_center):
        self.center = grav_center


