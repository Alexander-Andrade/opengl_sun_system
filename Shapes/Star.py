from Shapes.Circle import Circle

from Shapes.StarPainter import StarPainter
from Texture import Texture


class Star(Circle):

    def __init__(self, center, r, image_name):
        Circle.__init__(self, center, r)
        self.texture = Texture(image_name)
        self.painter = StarPainter(self)
