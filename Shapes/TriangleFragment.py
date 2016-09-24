from Texture import Texture
from Shapes.TriangleFragmentPainter import TriangleFragmentPainter
from Shapes.Triangle import Triangle
from Shapes.Point import Point
import numpy as np


class TriangleFragment(Triangle):

    def __init__(self, image_name, grav_center=Point(), size=1, life_epochs=0,
                 acceleration=np.zeros(3), attenuation=0, speed=np.zeros(3)):
        Triangle.__init__(self, grav_center, Point(grav_center.x + size, grav_center.y), Point(grav_center.x, grav_center.y + size))
        self.size = size
        self.texture = Texture(image_name)
        self.painter = TriangleFragmentPainter(self)
        self.life_epochs = life_epochs
        self.acceleration = acceleration
        self.attenuation = attenuation
        self.speed = speed
        self.vec_len = len(self.speed)

    def invert_speed(self, i, attenuation):
        self.speed[i] *= -1*attenuation

    def recalc_acceleration(self):
        for axis_accel in self.acceleration:
            if axis_accel > 0:
                axis_accel -= self.attenuation
                if axis_accel < 0:
                    axis_accel = 0

    # v = v0 +a*t
    def recalc_speed(self):
        for i in range(self.vec_len):
            self.speed[i] += self.acceleration[i]

    # uniformly accelerated motion
    # s = s0 + v0*t + a*(t^2)/2
    def recalc_grav_center_pos(self):
        center_arr = self.gravity_center().as_array()
        for i in range(self.vec_len):
            center_arr[i] = self.speed[i] + self.acceleration[i]
        self.set_gravitycenter(Point.from_array(center_arr))

    def update_position(self):
        if not self.is_time_over():
            self.life_epochs -= 1
            self.recalc_acceleration()
            self.recalc_grav_center_pos()
            self.recalc_speed()

    def is_time_over(self):
        return self.life_epochs > 0
