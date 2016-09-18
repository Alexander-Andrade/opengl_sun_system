import math

import Animation

from Shapes.Painter import *
import numpy as np

class EllipsePainter(Painter):
    
    def __init__(self, ellipse, n=50):
        self.ellipse = ellipse
        self.n = n
        self.dots = np.zeros((self.n, 3))
        self.fill_dots()

    def fill_dots(self):
        dt = Animation.sampling(self.n)
        for i in range(self.n):
            self.dots[i] = self.ellipse.parametric(i*dt).as_tuple()

    def draw(self):
        glBegin(GL_LINE_LOOP)
        glVertex3d(self.ellipse.center.x, self.ellipse.center.y, 0.0)
        for dot in self.dots:
            glVertex3d(dot[0], dot[1], dot[2])
        glEnd()
