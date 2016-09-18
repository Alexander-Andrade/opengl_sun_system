import math

import Animation

from Shapes.Painter import *


class OrbitPainter(Painter):
    def __init__(self, orbit, n=50):
        self.orbit = orbit
        self.n = n

    def draw(self):
        self.orbit.shape.draw()
