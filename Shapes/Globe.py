from Shapes.Circle import Circle

from Shapes.GlobePainter import GlobePainter
from Texture import Texture


class Globe(Circle):

    def __init__(self, center, r, image_name):
        Circle.__init__(self, center, r)
        self.texture = Texture(image_name)
        self.painter = GlobePainter(self)
