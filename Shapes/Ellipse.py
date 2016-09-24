import math

from Shapes.Point import Point
from Shapes.Shape import Shape
import Animation
import numpy as np

from Shapes.EllipsePainter import EllipsePainter


class Ellipse(Shape):
    
    def __init__(self, center=Point(), a=0.0, b=0.0, angle=0.0, point_of_rotation=None, has_painter=True):
        self.center = center
        self.point_of_rotation = point_of_rotation
        self.a = a
        self.b = b
        self.angle = math.radians(angle)
        if has_painter:
            self.painter = EllipsePainter(self)

    def parametric(self, t):
        x = self.center.x + self.a*math.cos(t)
        y = self.center.y + self.b*math.sin(t)
        if self.point_of_rotation:
            return Animation.rotate_around(self.point_of_rotation, Point(x, y), self.angle)

    def get_samples(self, n):
        dt = Animation.rad_angle_part(n)
        samples = np.zeros((n, 3))
        for i in range(n):
            samples[i] = self.parametric(i * dt).as_tuple()
        return samples

    def set_gravitycenter(self, grav_center):
        self.center = grav_center

    def gravity_center(self):
        return self.center

    @staticmethod
    def focal_dist(a, b):
        return (math.fabs(a**2-b**2))**(1/2)

    @staticmethod
    def find_center_from_focus(focus, a, b):
        return Point(focus.x - Ellipse.focal_dist(a, b), focus.y)
