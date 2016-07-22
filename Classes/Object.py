
import sys
sys.path.append('..')
import libtcodpy as lib
import Public.Functions as pf

class Object:
    def __init__(self, x, y, base_char, name, color, orientation):
        self.x = x
        self.y = y
        self.base_char = base_char
        self.name = name
        self.color = color
        self.orientation = orientation

    def move(self, dx, dy):
        # move by the given amount (dx, dy)
        self.x += dx
        self.y += dy

    def draw(self, console):
        self.console = console
        # define the character to be drawn, from within the base character
        self.define_char(self.base_char, self.orientation)
        CHAR_HEIGHT = len(self.char)
        CHAR_WIDTH = len(self.char[0])
        # get the center of the character(s) so we can draw in the right place
        (x_center, y_center) = pf.get_center(CHAR_HEIGHT, CHAR_WIDTH)
        for a in range(CHAR_HEIGHT):
            for b in range(CHAR_WIDTH):
                if self.char[a][b] != ' ':
                    lib.console_set_default_foreground(self.console, self.color)
                    lib.console_put_char(self.console, self.x - x_center + b, self.y - y_center + a, self.char[a][b], lib.BKGND_NONE)

    def clear(self, console):
        self.console = console
        # define the character to be drawn, from within the base character
        self.define_char(self.base_char, self.orientation)
        CHAR_HEIGHT = len(self.char)
        CHAR_WIDTH = len(self.char[0])
        # get the center of the character(s) so we can draw in the right place
        (x_center, y_center) = pf.get_center(CHAR_HEIGHT, CHAR_WIDTH)
        for y in range(CHAR_HEIGHT):
            for x in range(CHAR_WIDTH):
                if self.char[x][y] != ' ':
                    lib.console_set_default_foreground(self.console, self.color)
                    lib.console_put_char(self.console, self.x - x_center + y, self.y - y_center + x, ' ', lib.BKGND_NONE)



    def define_char(self, base_char, orientation):
        # defines the character to be displayed within the base character
        self.char = self.base_char[self.orientation]                    
