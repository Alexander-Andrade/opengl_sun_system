from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import *

from abc import ABCMeta, abstractmethod

class Painter(metaclass=ABCMeta):
 
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass



