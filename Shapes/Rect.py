from Shapes.Shape import Shape
from Shapes.Point import Point

class Rect(Shape):

    def __init__(self, point, width, height):
        self.point = point
        self.width = width
        self.height = height

    def points(self):
        return self.point, Point(self.point.x, self.point.y - self.height),\
               Point(self.point.x + self.width, self.point.y - self.height),\
               Point(self.point.x + self.width, self.point.y)

    def set_gravitycenter(self, grav_center):
        self.point = Point(grav_center.x-self.width/2, grav_center.y-self.height/2)

    def gravity_center(self):
        return Point(self.point.x + self.width/2, self.point.y + self.height/2)

    @staticmethod
    def from_circle(circle):
        p = Point(circle.center.x-circle.r, circle.center.y-circle.r)
        side = circle.r*2
        return Rect(p, side, side)

    def scale_on_center(self, scale):
        center = self.gravity_center()
        old_width= self.width
        old_height=self.height
        self.width *= scale
        self.height *= scale
        dx = (self.width - old_width)/2
        dy = (self.height - old_height)/2
        self.point = Point(center.x - dx, center.y - dy)

    def __repr__(self):
        return "Rect(p:{}, width:{}, height:{})".format(self.point, self.width, self.height)
