from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    def __init__(self):
        pass
    
    def draw(self):
        self.painter.draw()

    def setPainter(self, painter):
        self.painter = painter
    
    @abstractmethod
    def set_gravitycenter(self, grav_center):
        pass

