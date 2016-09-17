import math

import Animation

from Shapes.Painter import*


class CirclePainter(Painter):
    
    def __init__(self, circle, accuracy=50):
        self.circle = circle
        self.accuracy = accuracy

    def draw(self):
        x_coord = 0.0
        y_coord = 0.0
        dt = Animation.sampling(self.accuracy)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3d(self.circle.center.x, self.circle.center.y, 0.0)
        for i in range(self.accuracy+1):
            x_coord = self.circle.center.x + self.circle.r*math.cos(i*dt)
            y_coord = self.circle.center.y + self.circle.r*math.sin(i*dt)
            glVertex3d(x_coord, y_coord, 0.0)
        glEnd()



