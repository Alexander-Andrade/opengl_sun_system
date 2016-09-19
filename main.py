from OpenGL.GL import *
from OpenGL.GLUT import *

from Shapes import *


class Window:

    def __init__(self, application, **kwargs):
        self.application = application
        self.__init_window(**kwargs)
        self.__init_lightning()
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

    def __init_lightning(self):
        glEnable(GL_LIGHTING)
        glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
        

    def __register_app_event_handlers(self):
        glutDisplayFunc(self.application.display)

    def mainLoop(self):
        glutMainLoop()

class Application:

    def __init__(self):
        self.figures = []

    def create_shapes(self):
        self.figures.append(Background('images/space2.jpg'))

        self.figures.append(TriangleFragment(Point(0.23, 0.12), Point(0.32, 0.34), Point(0.54, 0,46), 'images/sun.jpg'))

        sun = Star(Point(0.0, 0.0), 0.15, 'images/sun.jpg')
        glize = Globe(Point(), 0.06, 'images/glize.jpg')
        mars = Globe(Point(), 0.034, 'images/mars.jpg')
        venus = Globe(Point(), 0.063, 'images/venus.jpg')
        calisto = Globe(Point(), 0.087, 'images/calisto.jpg')

        glize_orbit = Orbit(sun, glize, 50, 0.45, 0.43, 30)
        mars_orbit = Orbit(sun, mars, 47, 0.9, 0.87, 60)
        venus_orbit = Orbit(sun, venus, 38, 0.7, 0.65, 78)
        calisto_orbit = Orbit(sun, calisto, 25, 0.67, 0.6, 32)

        glize_orbit.start_moving_shape()
        mars_orbit.start_moving_shape()
        venus_orbit.start_moving_shape()
        calisto_orbit.start_moving_shape()

        self.figures.append(sun)
        self.figures.append(glize_orbit)
        self.figures.append(mars_orbit)
        self.figures.append(venus_orbit)
        self.figures.append(calisto_orbit)

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

