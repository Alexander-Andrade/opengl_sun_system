from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy as np

class Texture:

    def __init__(self, image_name):
        self.image = Image.open(image_name)
        self.img_data = np.array(list(self.image.getdata()), np.uint8)
        print(self.img_data.shape)
        # self.img_data = np.transpose(self.img_data, (1, 0, 2))
        # self.img_data2 = np.asarray(Image.open(image_name).transpose(Image.FLIP_TOP_BOTTOM), dtype=np.uint8)
        #print(self.img_data2.shape)
        self.texture = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.width(), self.height(), 0, GL_RGB, GL_UNSIGNED_BYTE, self.img_data)
        # gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGB, self.width(), self.height(), GL_RGB, GL_UNSIGNED_BYTE, self.img_data)


    def width(self):
        return self.image.size[0]

    def height(self):
        return self.image.size[1]