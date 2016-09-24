import math
import Animation
from Shapes.Painter import *
from Shapes.GlobePainter import GlobePainter


class StarPainter(GlobePainter):

    def __init__(self, globe, n=50):
        GlobePainter.__init__(self, globe, n)

    def draw(self):
        dt = Animation.rad_angle_part(self.n)
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        self.globe.texture.bind_texture()
        glBegin(GL_POLYGON)
        glNormal3f(0.0, 0.0, -1.0)
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


