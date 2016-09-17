from Shapes.Shape import Shape

from Shapes.BackgroundPainter import BackgroundPainter
from Texture import Texture


class Background(Shape):

    def __init__(self, image_name):
        self.texture = Texture(image_name)
        self.painter = BackgroundPainter(self)

    def set_gravitycenter(self, grav_center):
        raise NotImplementedError()
