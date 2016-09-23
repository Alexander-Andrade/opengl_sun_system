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

    def __init__(self, globe, n=50):
        self.globe = globe
        self.n = n

    def point_light(self, light_num, position):
        glEnable(light_num)
        glLightfv(light_num, GL_DIFFUSE, (0.4, 0.7, 0.2))
        glLightfv(light_num, GL_POSITION, position)
        glLightf(light_num, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(light_num, GL_LINEAR_ATTENUATION, 0.2)
        glLightf(light_num, GL_QUADRATIC_ATTENUATION, 0.4)

    def draw(self):
        glEnable(GL_LIGHT2)
        glLightfv(GL_LIGHT2, GL_DIFFUSE, (0.6, 0.2, 0.7))
        glLightfv(GL_LIGHT2, GL_POSITION, (0.0, 0.0, 0.1, 1.0))
        glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 0.0)
        glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.2)
        glLightf(GL_LIGHT2, GL_QUADRATIC_ATTENUATION, 0.2)

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
        #glDisable(GL_LIGHT2)
        glDisable(GL_TEXTURE_2D)


