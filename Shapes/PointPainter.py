from Shapes.Painter import *


class PointPainter(Painter):
    
    def __init__(self, point):
        self.point = point

    def draw(self):
        glColor3f(0.3, 0.7, 0.3)
        glPointSize(6.0)
        glBegin(GL_POINTS)
        glVertex3f(self.point.x, self.point.y, self.point.z)
        glEnd()
