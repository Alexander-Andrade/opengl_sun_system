from OpenGL.GL import *
from OpenGL.GLUT import *

from Shapes import *
from SequenceTimer import SequenceTimer


class Window:

    def __init__(self, application, **kwargs):
        self.application = application
        self.__init_window(**kwargs)
        self.__init_lightning()
        self.__gl_init()
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

    def __gl_init(self):
        # glClearColor(0.3, 0.3, 0.3, 0.0)
        pass

    def __init_lightning(self):
        # color search
        glEnable(GL_COLOR_MATERIAL)
        #glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
        glEnable(GL_NORMALIZE)

    def __register_app_event_handlers(self):
        glutDisplayFunc(self.application.display)

    def mainLoop(self):
        glutMainLoop()


def fu(_=None):
    print("Hello")

class Application:

    def __init__(self):
        self.figures = []
        self.sequenceTimer = SequenceTimer([(self.create_shapes, 0)])

    def create_shapes(self):
        self.figures.append(Background('images/space1.jpg'))

        sun = Globe(Point(0.0, 0.0), 0.12, 'images/sun.jpg')
        sun.set_painter(ShiningGlobePainter(sun))
        glize = Globe(Point(), 0.06, 'images/glize.jpg')
        mars = Globe(Point(), 0.034, 'images/mars.jpg')
        venus = Globe(Point(), 0.063, 'images/venus.jpg')
        calisto = Globe(Point(), 0.087, 'images/calisto.jpg')

        glize_orbit = Orbit(sun, glize, 50, 0.45, 0.43, 30)
        #mars_orbit = Orbit(sun, mars, 47, 0.9, 0.6, 60)
        venus_orbit = Orbit(sun, venus, 38, 0.7, 0.6, 78)
        calisto_orbit = Orbit(sun, calisto, 40, 0.56, 0.57, 32)

        glize_orbit.start_moving_shape()
        #mars_orbit.start_moving_shape()
        venus_orbit.start_moving_shape()
        calisto_orbit.start_moving_shape()

        self.figures.append(sun)
        self.figures.append(glize_orbit)
        #self.figures.append(mars_orbit)
        self.figures.append(venus_orbit)
        self.figures.append(calisto_orbit)

    def start_sequencetimer(self):
        self.sequenceTimer.start()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
        glEnable(GL_LIGHT2)
        glLightfv(GL_LIGHT2, GL_DIFFUSE, (0.4, 0.7, 0.2))
        glLightfv(GL_LIGHT2, GL_POSITION, (0.0, 0.0, -0.01, 1.0))
        glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 1.0)
        glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.8)
        glLightf(GL_LIGHT2, GL_QUADRATIC_ATTENUATION, 5)

        glColor3f(0.8, 0.8, 0.0)
        glBegin(GL_POLYGON)
        glNormal3f(0.0, 0.0, -1.0)
        glVertex3f(-1, -1, 0.0)
        glVertex3f(1, -1, 0.0)
        glVertex3f(1, 1, 0.0)
        glVertex3f(-1, 1, 0.0)
        glEnd()

        for figure in self.figures:
            figure.draw()

        glDisable(GL_LIGHT2)
        glFlush()
        glutSwapBuffers()

if __name__ == "__main__":
    glutInit(sys.argv)
    app = Application()
    window = Window(app)
    app.start_sequencetimer()
    window.mainLoop()

