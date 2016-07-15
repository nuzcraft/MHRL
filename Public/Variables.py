
# Public.Variables
# This document defines the public variables used in the project.

###chr definitions
# 30 solid up arrow
# 31 solid down arrow
# 186 double pipes vertical

# Size of the Window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

# size of the map
MAP_WIDTH = 80
MAP_HEIGHT = 40

# FPS Limit
LIMIT_FPS = 20

# Current Version
Version = '0.1'

# Player Variables
#Characters -- Must be Square, with an odd number on each side
player_north_char = ['  ' + chr(30) + '  '
                   , '  ' + chr(186) + '  '
                   , '  @  '
                   , '     '
                   , '     ']

player_south_char = ['     '
                   , '     '
                   , '  @  '
                   , '  ' + chr(186) + '  '
                   , '  ' + chr(31) + '  ']                   