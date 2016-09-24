from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import *


class Timer:

    def __init__(self, ms_duration, is_repeat, n_times=None):
        self.is_started = False
        self.is_repeat = is_repeat
        self.n_times = n_times
        self.ms_duration = ms_duration
        self.on_timer = None

    def timer(self, _=None):
        self.on_timer()
        if self.n_times:
            self.n_times -= 1
        if (self.is_repeat and self.is_started) or \
           (self.n_times and self.is_started):
            glutTimerFunc(self.ms_duration, self.timer, 0)
        else:
            self.is_started = False

    def start(self, on_timer):
        self.on_timer = on_timer
        if not self.is_started:
            glutTimerFunc(self.ms_duration, self.timer, None)
            self.is_started = True 

    def change_duration(self, ms_duration):
        self.stop()
        self.ms_duration = ms_duration
        self.start(self.on_timer)


    def stop(self):
        self.is_started = False

    


