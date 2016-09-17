from Shapes.Painter import *


class BackgroundPainter(Painter):

    def __init__(self, background):
        self.background = background

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        self.background.texture.bindTexture()
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex2f(-1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex2f(1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex2f(1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex2f(-1.0, 1.0)
        glEnd()
        glDisable(GL_TEXTURE_2D)
