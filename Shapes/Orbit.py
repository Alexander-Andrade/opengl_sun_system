import Animation
from Shapes.OrbitPainter import OrbitPainter
from Shapes.Trajectory import Trajectory

from Shapes.Ellipse import Ellipse


class Orbit(Trajectory, Ellipse):
    
    def __init__(self, shape, timerFreq, center, a, b, n=50):
        self.t = 0
        self.n = n
        self.dt = Animation.sampling(self.n)
        Trajectory.__init__(self, shape, timerFreq)
        Ellipse.__init__(self, center, a, b)
        self.shape.set_gravitycenter(self.cur_point)
        self.painter = OrbitPainter(self)

    def calc_next_trajpoint(self):
       self.cur_point = self.parametric(self.t)
       self.t += self.dt

