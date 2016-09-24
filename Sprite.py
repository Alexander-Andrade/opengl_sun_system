from Texture import Texture
from Shapes.Point import Point
from Shapes.Rect import Rect


class Sprite:

    def __init__(self, image_name, n_rows, n_cols, width, height):
        self.texture = Texture(image_name)
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.width = width
        self.height = height
        self.cur_row = 0
        self.cur_col = 0

    def get_rect(self, row, col):
        if (row < self.n_rows) and (col < self.n_cols):
            return Rect(Point(row*self.height, col*self.width), self.width, self.height)

    def __to_next_sprite(self):
        if self.cur_col < self.n_cols:
            self.cur_col += 1
        else:
            self.cur_col = 0
            self.cur_row += 1

        if self.cur_row < self.n_rows:
            self.cur_row += 1
        else:
            self.cur_col = 0
            self.cur_row = 0

    def next_sprite_rect(self):
        coord = self.get_rect(self.cur_row, self.cur_col)
        self.__to_next_sprite()
        return coord
