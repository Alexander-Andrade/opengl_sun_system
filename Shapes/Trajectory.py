from abc import abstractmethod

from OpenGL.GLUT import *
from Shapes.Shape import Shape

from Shapes.Point import Point
from Timer import Timer


class Trajectory(Shape):
   
    def __init__(self, shape, timerFreq):
        self.cur_point = Point()
        self.timer = Timer(timerFreq, True)
        self.shape = shape

    @abstractmethod
    def next_trajpoint(self):
        pass

    def move_shape(self):
        self.next_trajpoint()
        self.shape.set_gravitycenter(self.cur_point)

    def on_timer(self):
        self.move_shape()
        glutPostRedisplay()

    def start_moving_shape(self):
        self.timer.start(self.on_timer)

    def stop_moving_shape(self):
        self.timer.stop()

