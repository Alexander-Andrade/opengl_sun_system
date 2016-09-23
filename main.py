from OpenGL.GL import *
from OpenGL.GLUT import *

from Shapes import *


class Window:

    def __init__(self, application, **kwargs):
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
        self.__enable_lightning()

    def __enable_lightning(self):
        glEnable(GL_LIGHTING)
        # glEnable(GL_COLOR_MATERIAL)
        glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
        glEnable(GL_NORMALIZE)

    def __register_app_event_handlers(self):
        glutDisplayFunc(self.application.display)

    def mainLoop(self):
        glutMainLoop()

class Application:

    def __init__(self):
        self.figures = []

    def create_shapes(self):
        self.figures.append(Background('images/space1.jpg'))

        sun = Globe(Point(0.0, 0.0), 0.12, 'images/sun.jpg')
        sun.set_painter(ShiningGlobePainter(sun))
        glize = Globe(Point(), 0.06, 'images/glize.jpg')
        mars = Globe(Point(), 0.034, 'images/mars.jpg')
        venus = Globe(Point(), 0.063, 'images/venus.jpg')
        calisto = Globe(Point(), 0.087, 'images/calisto.jpg')

        glize_orbit = Orbit(sun, glize, 50, 0.45, 0.38, 30)
        mars_orbit = Orbit(sun, mars, 47, 0.9, 0.6, 60)
        venus_orbit = Orbit(sun, venus, 38, 0.7, 0.6, 78)
        calisto_orbit = Orbit(sun, calisto, 25, 0.67, 0.53, 32)

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

