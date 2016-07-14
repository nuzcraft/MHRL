
import sys
sys.path.append('..')
import libtcodpy as lib

class Object:
    def __init__(self, x, y, char, name, color):
        self.x = x
        self.y = y
        self.char = char
        self.name = name
        self.color = color

    def move(self, dx, dy):
        # move by the given amount (dx, dy)
        self.x += dx
        self.y += dy

    def draw(self, console):
        self.console = console
        lib.console_set_default_foreground(self.console, self.color)
        lib.console_put_char(self.console, self.x, self.y, self.char, lib.BKGND_NONE)       