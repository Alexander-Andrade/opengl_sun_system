from Shapes.Painter import *
from Shapes.Rect import Rect
from Shapes.Point import Point


class SpriteRectAnimationPainter(Painter):

    def __init__(self, sprite_rect):
        self.sprite_rect = sprite_rect

    def draw_rect(self, points):
        glTexCoord2f(points[0].x, points[0].y)
        glVertex2f(-1.0, 1.0)
        glTexCoord2f(points[1].x, points[1].y)
        glVertex2f(-1.0, -1.0)
        glTexCoord2f(points[2].x, points[2].y)
        glVertex2f(1.0, -1.0)
        glTexCoord2f(points[3].x, points[3].y)
        glVertex2f(1.0, 1.0)

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        self.sprite_rect.sprite.texture.bind_texture()
        rect_points = self.sprite_rect.rect.points()
        sprite_points = self.sprite_rect.sprite.next_sprite_rect().points()
        width = 0.125
        # 0.61
        height = 0.125
        rect = Rect(Point(width*4, 1-height*4), width, height)
        #rect = Rect(Point(0, 1), 1, 1)
        points = rect.points()
        print(rect)
        print(points)
        glBegin(GL_QUADS)
        # for i in range(4):
        #     glTexCoord2f(sprite_points[i].x, sprite_points[i].y)
        #     glVertex2f(rect_points[i].x, rect_points[i].y)
        # glEnd()
        glTexCoord2f(points[0].x, points[0].y)
        glVertex2f(-1.0, 1.0)
        glTexCoord2f(points[1].x, points[1].y)
        glVertex2f(-1.0, -1.0)
        glTexCoord2f(points[2].x, points[2].y)
        glVertex2f(1.0, -1.0)
        glTexCoord2f(points[3].x, points[3].y)
        glVertex2f(1.0, 1.0)
        glEnd()
        glDisable(GL_TEXTURE_2D)
