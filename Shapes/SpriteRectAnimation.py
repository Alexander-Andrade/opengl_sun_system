from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Texture import Texture
from Timer import Timer
from Shapes.Point import Point
from Shapes.Rect import Rect
from Sprite import Sprite
from Shapes.Shape import Shape
from OpenGL.GLUT import*
from Shapes.SpriteRectAnimationPainter import SpriteExplosionPainter


class SpriteRectAnimation(Shape):

    def __init__(self, sprite, rect, n_frames, ms_duration, light=GL_LIGHT0):
        self.sprite = sprite
        self.rect = rect
        self.timer = Timer(ms_duration, False, n_frames)
        self.painter = SpriteExplosionPainter(self, light)

    def set_gravitycenter(self, grav_center):
        self.rect.set_gravitycenter(grav_center)

    def gravity_center(self):
        return self.rect.gravity_center()

    def animate(self):
        self.sprite.to_next_sprite()
        glutPostRedisplay()

    def start(self):
        self.timer.start(self.animate)




