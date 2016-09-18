import Animation
from Shapes.OrbitPainter import OrbitPainter
from Shapes.Trajectory import Trajectory
from Shapes.Point import Point
from Shapes.Ellipse import Ellipse


class Orbit(Trajectory, Ellipse):
    
    def __init__(self, globe, satellite, timer_freq, a, b, angle=0.0, n=100):
        self.n = n
        Trajectory.__init__(self, satellite, timer_freq)
        Ellipse.__init__(self, Ellipse.find_center_from_focus(globe.center, a, b), a, b, angle, globe.center, False)
        self.points = self.get_samples(self.n)
        self.i = 0
        self.painter = OrbitPainter(self)

    def next_trajpoint(self):
        if self.i == self.n:
            self.i = 0
        self.cur_point = Point.from_tuple(self.points[self.i])
        self.i += 1

