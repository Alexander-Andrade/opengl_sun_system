from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import sys
from Point import Point
from Circle import Circle
from Timer import Timer
from Trajectory import Trajectory
from Ellipse import Ellipse
from EllipsePainter import RotatedEllipsePainter
from Orbit import Orbit

class Window:

    def __init__(self, application,**kwargs):
        self.application = application
        self.__init_window(**kwargs)
        self.__register_app_event_handlers()

    def __init_window(self, **kwargs):
        self.init_window_pos = kwargs.get('init_window_pos', (100, 100))
        self.title = kwargs.get('title', 'window')
        self.init_wind_size = kwargs.get('init_wind_size', (600, 600))
        self.display_mode = kwargs.get('display_mode', GLUT_DOUBLE | GLUT_RGB)
        glutInitDisplayMode(self.display_mode)
        glutInitWindowSize(self.init_wind_size[0], self.init_wind_size[1])
        glutInitWindowPosition(self.init_window_pos[0], self.init_window_pos[1])
        glutCreateWindow(self.title)
        

    def __register_app_event_handlers(self):
        glutDisplayFunc(self.application.display)

    def mainLoop(self):
        glutMainLoop()

class Application:

    def __init__(self):
        self.figures = []
        #self.figures.append(Point(0.2, 0.12, 0.34))
        #self.figures.append(Circle(Point(0.12, 0.342, 0.34), 0.4))
        #self.figures.append(Ellipce(Point(0.1, 0.43),0.1, 0.23))

        point = Point(0.2, 0.7)
        orbit = Orbit(point, 50, Point(0.5, 0.5), 0.4, 0.1)
        orbit.start_moving_shape()
        self.figures.append(orbit)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.0, 0.3, 0.0)
        for figure in self.figures:
            figure.draw()
        glutSwapBuffers()


if __name__ == "__main__":
    glutInit(sys.argv)
    app = Application()
    window = Window(app)
     
    window.mainLoop()
