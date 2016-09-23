import math

import Animation

from Shapes.Painter import *


class GlobePainter(Painter):

    def __init__(self, globe, n=50):
        self.globe = globe
        self.n = n

    def draw(self):
        dt = Animation.sampling(self.n)
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


class ShiningGlobePainter(Painter):

    def __init__(self, globe, n=50, light=GL_LIGHT0):
        self.globe = globe
        self.n = n
        self.light = light

    def point_light(self):
        glEnable(self.light)
        glLightfv(self.light, GL_DIFFUSE, (0.6, 0.2, 0.7))
        pos = self.globe.center.as_tuple()
        glLightfv(self.light, GL_POSITION, (pos[0], pos[1], 0.1, 1.0))
        glLightf(self.light, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(self.light, GL_LINEAR_ATTENUATION, 0.2)
        glLightf(self.light, GL_QUADRATIC_ATTENUATION, 0.2)

    def draw(self):
        glEnable(GL_LIGHT2)
        self.point_light()
        # glLightfv(GL_LIGHT2, GL_DIFFUSE, (0.6, 0.2, 0.7))
        # glLightfv(GL_LIGHT2, GL_POSITION, (0.0, 0.0, 0.1, 1.0))
        # glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 0.0)
        # glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.2)
        # glLightf(GL_LIGHT2, GL_QUADRATIC_ATTENUATION, 0.2)

        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
        dt = Animation.sampling(self.n)
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


