from Shapes.Shape import Shape
from Shapes.Point import Point


class Triangle(Shape):

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def set_gravitycenter(self, grav_center):
        center = self.gravitycenter()
        diff = grav_center - center
        self.p1 = self.p1 + diff
        self.p2 = self.p2 + diff
        self.p3 = self.p3 + diff

    def __repr__(self):
        return "Triangle(p1:{}, p2:{}, p3:{})".format(self.p1, self.p2, self.p3)

    def gravity_center(self):
        x_coord = (self.p1.x + self.p2.x + self.p3.x)/3
        y_coord = (self.p1.y + self.p2.y + self.p3.y)/3
        z_coord = (self.p1.z + self.p2.z + self.p3.z)/3
        return Point(x_coord, y_coord, z_coord)

