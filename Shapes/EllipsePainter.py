import math

import Animation

from Shapes.Painter import *


class EllipsePainter(Painter):
    
    def __init__(self, ellipse, n=50):
        self.ellipse = ellipse
        self.n = n
        
    def draw(self):
        dt = Animation.sampling(self.n)
        glBegin(GL_LINE_LOOP)
        glVertex3d(self.ellipse.center.x, self.ellipse.center.y, 0.0)
        for i in range(self.n+1):
            x_coord = self.ellipse.center.x + self.ellipse.a*math.cos(i*dt)
            y_coord = self.ellipse.center.y + self.ellipse.b*math.sin(i*dt)
            glVertex3d(x_coord, y_coord, 0.0)
        glEnd()


class RotatedEllipsePainter(Painter):
    def __init__(self, ellipse, n=50):
        self.ellipse = ellipse
        self.n = n

    def draw(self):
        dt = Animation.sampling(self.n)
        glPushMatrix()
        glRotatef(240, 1.0, 1.0, 0.0)
        glTranslatef(0.3, 0.4, 0.0)
        glBegin(GL_LINE_LOOP)
        glVertex3d(self.ellipse.center.x, self.ellipse.center.y, 0.0)
        for i in range(self.n + 1):
            x_coord = self.ellipse.center.x + self.ellipse.a * math.cos(i * dt)
            y_coord = self.ellipse.center.y + self.ellipse.b * math.sin(i * dt)
            glVertex3d(x_coord, y_coord, 0.0)
        glEnd()
        glPopMatrix()
