import math

import Animation

from Shapes.Painter import *

class EllipsePainter(Painter):
    
    def __init__(self, ellipse, n=50):
        self.ellipse = ellipse
        self.n = n
        self.samples = self.ellipse.get_samples(self.n)

    def draw(self):
        glBegin(GL_LINE_LOOP)
        glVertex3d(self.ellipse.center.x, self.ellipse.center.y, 0.0)
        for sample in self.samples:
            glVertex3d(sample[0], sample[1], sample[2])
        glEnd()
