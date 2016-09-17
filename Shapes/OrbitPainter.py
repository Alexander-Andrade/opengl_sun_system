import math

import Animation

from Shapes.Painter import *


class OrbitPainter(Painter):
    def __init__(self, orbit, n=50):
        self.orbit = orbit
        self.n = n

    def draw(self):
        dt = Animation.sampling(self.n)
        glPushMatrix()
        glRotatef(240, 1.0, 1.0, 0.0)
        glTranslatef(0.3, -0.4, 0.0)
        glBegin(GL_LINE_LOOP)
        glVertex3d(self.orbit.center.x, self.orbit.center.y, 0.0)
        for i in range(self.n + 1):
            x_coord = self.orbit.center.x + self.orbit.a * math.cos(i * dt)
            y_coord = self.orbit.center.y + self.orbit.b * math.sin(i * dt)
            glVertex3d(x_coord, y_coord, 0.0)
        glEnd()
        self.orbit.shape.draw()
        glPopMatrix()
