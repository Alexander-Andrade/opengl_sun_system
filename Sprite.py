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
            return Rect(Point(col*self.width, 1-row*self.height), self.width, self.height)

    def to_next_sprite(self):
        if self.cur_col < self.n_cols-1:
            self.cur_col += 1
        else:
            self.cur_col = 0
            self.cur_row += 1


    def cur_sprite_rect(self):
        return self.get_rect(self.cur_row, self.cur_col)
