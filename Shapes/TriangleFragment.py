from Shapes.Shape import Shape
from Texture import Texture
from Shapes.TriangleFragmentPainter import TriangleFragmentPainter
from Shapes.Point import Point


class TriangleFragment(Shape):

    def __init__(self, image_name, grav_center=Point(), side_size=1, life_epochs=0,
                 acceleration=(0.0, 0.0, 0.0), attenuation=0, speed=(0.0, 0.0, 0.0)):
        self.p1 = Point()
        self.p2 = Point()
        self.p3 = Point()
        self.side_size = side_size
        self.texture = Texture(image_name)
        self.painter = TriangleFragmentPainter(self)
        self.life_epochs = life_epochs
        self.acceleration = acceleration
        self.attenuation = attenuation
        self.speed = speed

    def set_points(self, grav_center, side_size):
        self.p1 = grav_center
        self.p2 = Point(grav_center.x + side_size, grav_center.y)
        self.p3 =

    def set_gravitycenter(self, grav_center):
        self.p1 = grav_center

    def invert_speed(self, i, attenuation):
        self.speed[i] *= -1*attenuation

    def recalc_acceleration(self):
        for axis_accel in self.acceleration:
            if axis_accel > 0:
                axis_accel -= self.attenuation

    def recalc_grav_center_pos(self):
        center = self.gravitycenter()
        for i in range(center):


    def update_position(self):
        self.life_epochs -= 1
        self.recalc_acceleration()

