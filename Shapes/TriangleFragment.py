from Shapes.Triangle import Triangle
from Texture import Texture
from Shapes.TriangleFragmentPainter import TriangleFragmentPainter

class TriangleFragment(Triangle):

    def __init__(self, p1, p2, p3, image_name):
        Triangle.__init__(self, p1, p2, p3)
        self.texture = Texture(image_name)
        self.painter = TriangleFragmentPainter(self)
