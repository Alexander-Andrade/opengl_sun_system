from Shapes.Painter import *
from Shapes.Rect import Rect
from Shapes.Point import Point


class SpriteExplosionPainter(Painter):

    def __init__(self, sprite_rect, light=GL_LIGHT0):
        self.sprite_rect = sprite_rect
        self.light = light

    def point_light(self, center):
        glEnable(self.light)
        glLightfv(self.light, GL_DIFFUSE, (0.6, 0.2, 0.7))
        glLightfv(self.light, GL_SPECULAR, (0.7, 0.2, 0.2))
        center = center.as_tuple()
        glLightfv(self.light, GL_POSITION, (center[0], center[1], 0.1, 1.0))
        glLightf(self.light, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(self.light, GL_LINEAR_ATTENUATION, 0.2)
        glLightf(self.light, GL_QUADRATIC_ATTENUATION, 0.2)

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_COMBINE)
        glTexEnvf(GL_TEXTURE_ENV, GL_COMBINE_RGB, GL_MODULATE)
        self.sprite_rect.sprite.texture.bind_texture()
        rect_points = self.sprite_rect.rect.points()
        sprite_points = self.sprite_rect.sprite.cur_sprite_rect().points()
        self.point_light(self.sprite_rect.rect.gravity_center())
        glBegin(GL_QUADS)
        for i in range(4):
            glTexCoord2f(sprite_points[i].x, sprite_points[i].y)
            glVertex2f(rect_points[i].x, rect_points[i].y)
        glEnd()
        glDisable(self.light)
        glDisable(GL_TEXTURE_2D)
