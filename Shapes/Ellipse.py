import math

from Shapes.Point import Point
from Shapes.Shape import Shape
import Animation
import numpy as np

from Shapes.EllipsePainter import EllipsePainter


class Ellipse(Shape):
    
    def __init__(self, center=Point(), a=0.0, b=0.0, angle=0.0, rotate_point=None, has_painter=True):
        self.center = center
        self.a = a
        self.b = b
        self.angle = math.radians(angle)
        self.rotate_point = rotate_point
        if has_painter:
            self.painter = EllipsePainter(self)

    def parametric(self, t):
        x = self.center.x + self.a*math.cos(t)
        y = self.center.y + self.b*math.sin(t)
        return Animation.rotate_around(self.rotate_point, Point(x, y), self.angle)

    def get_samples(self, n):
        dt = Animation.sampling(n)
        samples = np.zeros((n, 3))
        for i in range(n):
            samples[i] = self.parametric(i * dt).as_tuple()
        return samples

    def set_gravitycenter(self, grav_center):
        self.center = grav_center

    @staticmethod
    def focal_dist(a, b):
        return (math.fabs(a**2-b**2))**(1/2)

    @staticmethod
    def find_center_from_focus(focus, a, b):
        return Point(focus.x - Ellipse.focal_dist(a, b), focus.y)
