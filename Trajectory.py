from abc import ABCMeta, abstractmethod

from OpenGL.GLUT import *
from Shape import Shape
from Point import Point
from Timer import Timer

class Trajectory(Shape):
   
   def __init__(self, shape, timerFreq):
       self.cur_point = Point()
       self.timer = Timer(timerFreq, True)
       self.shape = shape

   @abstractmethod
   def calc_next_trajpoint(self):
       pass 

   def move_shape(self):
       self.calc_next_trajpoint()
       self.shape.set_gravitycenter(self.cur_point)

   def on_timer(self):
       self.move_shape()
       glutPostRedisplay()

   def start_moving_shape(self):
       self.timer.start(self.on_timer)

   def stop_moving_shape(self):
       self.timer.stop()

   
