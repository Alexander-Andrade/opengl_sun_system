from abc import ABCMeta, abstractmethod
from Shapes.Point import Point
from OpenGL.GLUT import *
from Shapes.Painter import Painter
from Timer import Timer
from Sprite import Sprite
import math

def rotate_around(center, point, angle):
    x = (point.x - center.x) * math.cos(angle) - (point.y - center.y) * math.sin(angle) + center.x
    y = (point.y - center.y) * math.cos(angle) + (point.x - center.x) * math.sin(angle) + center.y
    return Point(x, y)

def rad_angle_part(n):
    return 2.0 * math.pi / (n - 1)


class SpriteAnimation(Sprite):

    def __init__(self, image_name, n_rows, n_cols, ms, n_frames):
        Sprite.__init__(self, image_name, n_rows, n_cols)
        self.timer = Timer(ms, False, n_frames)

    def start_animation(self):
        self.timer.start(self.animate)

    def animate(self):
        self.to_next_sprite()
        glutPostRedisplay()

    def stop_animation(self):
        self.timer.stop()


