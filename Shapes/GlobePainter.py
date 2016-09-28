import math

import Animation

from Shapes.Painter import *
from Timer import Timer
from Shapes.Rect import Rect


class GlobePainter(Painter):

    def __init__(self, globe, n=50):
        self.globe = globe
        self.n = n

    def draw(self):
        dt = Animation.rad_angle_part(self.n)
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
        self.globe.texture.bind_texture()
        glBegin(GL_POLYGON)
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3d(self.globe.center.x, self.globe.center.y, 0.0)

        for angle in range(0, 362, 2):
            radian = angle * (math.pi / 180.0)

            xcos = math.cos(radian)
            ysin = math.sin(radian)
            x = xcos * self.globe.r + self.globe.center.x
            y = ysin * self.globe.r + self.globe.center.y
            tx = xcos * 0.5 + 0.5
            ty = ysin * 0.5 + 0.5

            glTexCoord2f(tx, ty)
            glVertex2f(x, y)

        glEnd()
        glDisable(GL_TEXTURE_2D)


class GlobeSpriteAnimationPainter(Painter):

    def __init__(self, globe, animation, light=GL_LIGHT0):
        self.globe = globe
        self.animation = animation
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
        self.animation.texture.bind_texture()
        rect = Rect.from_circle(self.globe)
        rect.scale_on_center(2)
        rect_points = rect.points()
        sprite_points = self.animation.cur_sprite_rect().points()
        self.point_light(self.globe.center)
        glBegin(GL_QUADS)
        for i in range(4):
            glTexCoord2f(sprite_points[i].x, sprite_points[i].y)
            glVertex2f(rect_points[i].x, rect_points[i].y)
        glEnd()
        glDisable(self.light)
        glDisable(GL_TEXTURE_2D)


class ShiningGlobePainter(Painter):

    def __init__(self, globe, n=50, light=GL_LIGHT0):
        self.globe = globe
        self.n = n
        self.light = light

    def point_light(self):
        glEnable(self.light)
        glLightfv(self.light, GL_DIFFUSE, (0.6, 0.2, 0.7))
        glLightfv(self.light, GL_SPECULAR, (0.7, 0.2, 0.2))
        pos = self.globe.center.as_tuple()
        glLightfv(self.light, GL_POSITION, (pos[0], pos[1], 0.1, 1.0))
        glLightf(self.light, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(self.light, GL_LINEAR_ATTENUATION, 0.2)
        glLightf(self.light, GL_QUADRATIC_ATTENUATION, 0.2)

    def draw(self):
        self.point_light()

        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
        dt = Animation.rad_angle_part(self.n)
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
        self.globe.texture.bind_texture()

        glBegin(GL_POLYGON)
        glVertex3d(self.globe.center.x, self.globe.center.y, 0.0)

        for angle in range(0, 362, 2):
            radian = angle * (math.pi / 180.0)

            xcos = math.cos(radian)
            ysin = math.sin(radian)
            x = xcos * self.globe.r + self.globe.center.x
            y = ysin * self.globe.r + self.globe.center.y
            tx = xcos * 0.5 + 0.5
            ty = ysin * 0.5 + 0.5

            glTexCoord2f(tx, ty)
            glVertex2f(x, y)
        glEnd()
        glDisable(GL_TEXTURE_2D)


class DummyGlobePainter(Painter):

    def __init__(self, globe):
        self.globe = globe

    def draw(self):
        pass

