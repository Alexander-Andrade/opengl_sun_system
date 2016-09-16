from Painter import *
import Animation
import math

class EllipsePainter(Painter):
    
    def __init__(self, ellipse, accuracy=50):
        self.ellipse = ellipse
        self.accuracy = accuracy
        
    def draw(self):
        dt = Animation.sampling(self.accuracy)
        glBegin(GL_LINE_LOOP)
        glVertex3d(self.ellipse.center.x, self.ellipse.center.y, 0.0)
        for i in range(self.accuracy+1):
            x_coord = self.ellipse.center.x + self.ellipse.a*math.cos(i*dt)
            y_coord = self.ellipse.center.y + self.ellipse.b*math.sin(i*dt)
            glVertex3d(x_coord, y_coord, 0.0)
        glEnd()

