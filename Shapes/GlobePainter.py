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
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        self.globe.texture.bindTexture()
        glBegin(GL_POLYGON)
        glVertex3d(self.globe.center.x, self.globe.center.y, 0.0)

        for angle in range(0, 360, 2):
            radian = angle * (math.pi / 180.0)

            xcos = math.cos(radian)
            ysin = math.sin(radian)
            x = xcos * self.globe.r + self.globe.center.x
            y = ysin * self.globe.r + self.globe.center.y
            tx = xcos * 0.5 + 0.5
            ty = ysin * 0.5 + 0.5

            glTexCoord2f(tx, ty)
            glVertex2f(x, y)


        # for i in range(self.n + 1):
        #     x_coord = self.globe.center.x + self.globe.r * math.cos(i * dt)
        #     y_coord = self.globe.center.y + self.globe.r * math.sin(i * dt)
        #     glVertex3d(x_coord, y_coord, 0.0)
        #     glTexCoord2f(x_coord, y_coord, 0.0)
        #     radian = angle * (math.pi / 180.0)
        #     xcos = math.cos(radian)
        #     ysin = (float)
        #     sin(radian);
        #     x = xcos * c.r + c.pos.x;
        #     y = ysin * c.r + c.pos.y;
        #     tx = xcos * 0.5 + 0.5;
        #     ty = ysin * 0.5 + 0.5;
        #
        #     glTexCoord2f(tx, ty);
        #     glVertex2f(x, y);
        glEnd()
        glDisable(GL_TEXTURE_2D)

