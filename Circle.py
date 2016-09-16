from Shape import Shape
from CirclePainter import CirclePainter

class Circle(Shape):
   
    def __init__(self, center, r):
        self.center = center
        self.r = r
        self.painter = CirclePainter(self, 50)
        
    def set_gravitycenter(self, grav_center):
        self.center = grav_center



