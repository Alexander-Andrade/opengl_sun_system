from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy as np


class Texture:

    def __init__(self, image_name, type=GL_TEXTURE_2D):
        self.type = type
        self.image = Image.open(image_name).transpose(Image.FLIP_LEFT_RIGHT).rotate(180)
        self.img_data = np.array(list(self.image.getdata()), np.uint8)
        glEnable(GL_TEXTURE_2D)
        self.texture = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glBindTexture(type, self.texture)
        glTexParameteri(type, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(type, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(type, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(type, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        # glTexImage2D(type, 0, GL_RGB, self.width(), self.height(), 0, GL_RGB, GL_UNSIGNED_BYTE, self.img_data)
        im_format = self.image_gl_format(self.img_data)
        gluBuild2DMipmaps(type, im_format, self.width(), self.height(), im_format, GL_UNSIGNED_BYTE, self.img_data)

    def image_gl_format(self, img_data):
        return GL_RGBA if len(img_data[0]) == 4 else GL_RGB


    def bind_texture(self):
        glBindTexture(self.type, self.texture)

    def width(self):
        return self.image.size[0]

    def height(self):
        return self.image.size[1]