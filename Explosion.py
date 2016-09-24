from Shapes.TriangleFragment import TriangleFragment
from Timer import Timer
import random
import numpy as np
# (self, image_name, grav_center, size, life_epochs,
# acceleration, attenuation, speed)

class Explosion:

    def __init__(self, center, radius, acceleration, n_fragments, n_life_epochs, ms_duration):
        self.timer = Timer(ms_duration, True)
        self.center = center
        self.radius = radius
        self.fragments = []
        self.n_life_epochs = n_life_epochs
        self.acceleration = acceleration
        self.n_fragments = n_fragments

    def rand_explode_coords(self):
        x_coord = random.uniform(self.center.x-self.radius, self.center.x+self.radius)
        y_coord = random.uniform(self.center.y - self.radius, self.center.y + self.radius)
        z_coord = random.uniform(self.center.z - self.radius, self.center.z + self.radius)



    def init_fragments(self):
        for i in range(self.n_fragments):
            pass


    def explode(self):
        pass

    def start(self):
        self.timer.start(self.explode)

    def stop(self):
        self.timer.stop()
