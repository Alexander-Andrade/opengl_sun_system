from Shapes.Painter import *
import math


class TriangleFragmentPainter(Painter):

    def __init__(self, frag):
        self.frag = frag

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        self.frag.texture.bind_texture()
        glBegin(GL_TRIANGLE_FAN)
        glTexCoord2f(self.frag.p1.x, self.frag.p1.y)
        glVertex2f(self.frag.p1.x, self.frag.p1.y)
        glTexCoord2f(self.frag.p2.x, self.frag.p2.y)
        glVertex2f(self.frag.p2.x, self.frag.p2.y)
        glTexCoord2f(self.frag.p3.x, self.frag.p3.y)
        glVertex2f(self.frag.p3.x, self.frag.p3.y)
        glEnd()
        glDisable(GL_TEXTURE_2D)
