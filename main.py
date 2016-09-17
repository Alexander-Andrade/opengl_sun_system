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
from Texture import Texture
from Background import Background

class Window:

    def __init__(self, application,**kwargs):
        self.application = application
        self.__init_window(**kwargs)
        self.__register_app_event_handlers()

    def __init_window(self, init_window_pos=(100, 100), title='window', init_wind_size=(600, 600),
                      display_mode=GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH):
        self.init_window_pos = init_window_pos
        self.title = title
        self.init_wind_size = init_wind_size
        self.display_mode = display_mode
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

    def create_shapes(self):
        self.figures.append(Background('images/space1.jpg'))
        point = Point(0.2, 0.7)
        orbit = Orbit(point, 50, Point(0.5, 0.5), 0.4, 0.1)
        orbit.start_moving_shape()
        self.figures.append(orbit)
        self.figures.append(Ellipse(Point(0.1, 0.43), 0.1, 0.23))

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glColor3f(0.0, 0.8, 0.0)

        for figure in self.figures:
            figure.draw()
        glFlush()
        glutSwapBuffers()


if __name__ == "__main__":
    glutInit(sys.argv)
    app = Application()
    window = Window(app)
    app.create_shapes()
    window.mainLoop()

