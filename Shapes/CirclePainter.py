import math

import Animation

from Shapes.Painter import*


class CirclePainter(Painter):
    
    def __init__(self, circle, n=50):
        self.circle = circle
        self.n = n

    def draw(self):
        dt = Animation.sampling(self.n)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3d(self.circle.center.x, self.circle.center.y, 0.0)
        for i in range(self.n+1):
            x_coord = self.circle.center.x + self.circle.r*math.cos(i*dt)
            y_coord = self.circle.center.y + self.circle.r*math.sin(i*dt)
            glVertex3d(x_coord, y_coord, 0.0)
        glEnd()



