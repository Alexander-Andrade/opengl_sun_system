from OpenGL.GL import *
from OpenGL.GLUT import *

from Shapes import *
from SequenceTimer import SequenceTimer
from Timer import Timer
from Sprite import Sprite
import random

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


class Application:

    def __init__(self):
        self.background = None
        self.star = None
        self.orbits = []
        self.sequenceTimer = SequenceTimer([(self.create_shapes, 0)])

    def explode_random_planet(self):
        orbit = random.choice(self.orbits)
        self.orbits.remove(orbit)
        sprite = Sprite('images/sprites/explode_9.jpg', 5, 4, 0.25, 0.2)
        sprite_anim = SpriteRectAnimation(sprite, Rect.from_circle(orbit), 19, 1000, GL_LIGHT1)
        sprite_anim.start()
        self.orbits.append(sprite_anim)

    def create_shapes(self):
        self.background = Background('images/globes/space1.jpg')

        self.star = Globe(Point(0.0, 0.0), 0.12, 'images/globes/sun.jpg')
        self.star.set_painter(ShiningGlobePainter(self.star))

        glize = Globe(Point(), 0.06, 'images/globes/glize.jpg')
        mars = Globe(Point(), 0.034, 'images/globes/mars.jpg')
        venus = Globe(Point(), 0.063, 'images/globes/venus.jpg')
        calisto = Globe(Point(), 0.087, 'images/globes/calisto.jpg')

        glize_orbit = Orbit(self.star, glize, 50, 0.45, 0.43, 30)
        mars_orbit = Orbit(self.star, mars, 47, 0.9, 0.6, 60)
        venus_orbit = Orbit(self.star, venus, 38, 0.7, 0.6, 78)
        calisto_orbit = Orbit(self.star, calisto, 40, 0.56, 0.57, 32)

        glize_orbit.start_moving_shape()
        mars_orbit.start_moving_shape()
        venus_orbit.start_moving_shape()
        calisto_orbit.start_moving_shape()

        self.orbits.append(glize_orbit)
        self.orbits.append(mars_orbit)
        self.orbits.append(venus_orbit)
        self.orbits.append(calisto_orbit)

    def start_sequencetimer(self):
        self.sequenceTimer.start()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.background.draw()
        self.star.draw()

        for figure in self.orbits:
            figure.draw()

        glFlush()
        glutSwapBuffers()


if __name__ == "__main__":
    glutInit(sys.argv)
    app = Application()
    window = Window(app)
    app.start_sequencetimer()
    window.mainLoop()
