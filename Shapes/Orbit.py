import Animation
from Shapes.OrbitPainter import OrbitPainter
from Shapes.Trajectory import Trajectory
from Shapes.Point import Point
from Shapes.Ellipse import Ellipse
import Animation

class Orbit(Trajectory, Ellipse):
    
    def __init__(self, globe, satellite, timer_freq, a, b, angle=0.0, n=100, t=0.0):
        self.n = n
        self.globe = globe
        Trajectory.__init__(self, satellite, timer_freq)
        Ellipse.__init__(self, Ellipse.find_center_from_focus(globe.center, a, b), a, b, angle, globe.center, False)
        self.t = t
        self.dt = Animation.rad_angle_part(n)
        self.painter = OrbitPainter(self)

    def next_trajpoint(self):
        #center = Ellipse.find_center_from_focus(self.globe.center, self.a, self.b)
        p = Animation.rotate_around(self.globe.center, Ellipse.find_center_from_focus(self.globe.center, self.a, self.b), self.angle)
        self.set_gravitycenter(p)

        self.cur_point = self.parametric(self.t)
        self.t += self.dt

    def set_gravitycenter(self, grav_center):
        Ellipse.set_gravitycenter(self, grav_center)