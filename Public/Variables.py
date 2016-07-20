import sys
sys.path.append('..')
import libtcodpy as lib

# Public.Variables
# This document defines the public variables used in the project.

###chr definitions
# 16 solid right arrow
# 17 solid left arrow
# 30 solid up arrow
# 31 solid down arrow
# 186 double pipes vertical
# 205 double pipes horizontal

# Size of the Window
SCREEN_WIDTH = 140      
SCREEN_HEIGHT = 80

# size of the map i.e. playable area
MAP_WIDTH = 115
MAP_HEIGHT = 65

MAP_Y = 15 # location of map on screen

# FPS Limit
LIMIT_FPS = 60

# Current Version
Version = 'a:0.1'

# Control variables
key = lib.Key()
mouse = lib.Mouse()

# Player Variables
#Characters -- Must be Square, with an odd number on each side
player_greatsword_char = {
'north': ['  ' + chr(30) + '  '
        , '  ' + chr(186) + '  '
        , '  @  '
        , '     '
        , '     ']
, 'south': ['     '
          , '     '
          , '  @  '
          , '  ' + chr(186) + '  '
          , '  ' + chr(31) + '  ']
, 'east': ['     '
         , '     '
         , '  @' + chr(205) + chr(16)
         , '     '
         , '     ']
, 'west': ['     '
         , '     '
         , chr(17) + chr(205) + '@  '
         , '     '
         , '     ']}               
