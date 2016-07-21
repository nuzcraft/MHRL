import sys
sys.path.append('..')
import libtcodpy as lib

# Public.Variables
# This document defines the public variables used in the project.

# chr definitions
solid_r_arrow = chr(16)
solid_l_arrow = chr(17)
solid_u_arrow = chr(30)
solid_d_arrow = chr(31)

dbl_pipes_vert = chr(186)
dbl_pipes_horiz = chr(205)

# Size of the Window
SCREEN_WIDTH = 140      
SCREEN_HEIGHT = 80

# Main con variables
MAIN_CON_WIDTH = 115
MAIN_CON_HEIGHT = 65
MAIN_CON_Y = 15 # location of map on screen

# Status con variables
STATUS_CON_WIDTH = 115
STATUS_CON_HEIGHT = 15

# Map con variables
MAP_CON_WIDTH = 25
MAP_CON_HEIGHT = 25
MAP_CON_X = 115

# Menu con variables
MENU_CON_WIDTH = 25
MENU_CON_HEIGHT = 55
MENU_CON_X = 115
MENU_CON_Y = 25

# create new consoles
main_con = lib.console_new(MAIN_CON_WIDTH, MAIN_CON_HEIGHT)
status_con = lib.console_new(STATUS_CON_WIDTH, STATUS_CON_HEIGHT)
map_con = lib.console_new(MAP_CON_WIDTH, MAP_CON_HEIGHT)
menu_con = lib.console_new(MENU_CON_WIDTH, MENU_CON_HEIGHT)

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
'north': ['  ' + solid_u_arrow + '  '
        , '  ' + dbl_pipes_vert + '  '
        , '  @  '
        , '     '
        , '     ']
, 'south': ['     '
          , '     '
          , '  @  '
          , '  ' + dbl_pipes_vert + '  '
          , '  ' + solid_d_arrow + '  ']
, 'east': ['     '
         , '     '
         , '  @' + dbl_pipes_horiz + solid_r_arrow
         , '     '
         , '     ']
, 'west': ['     '
         , '     '
         , solid_l_arrow + dbl_pipes_horiz + '@  '
         , '     '
         , '     ']}    

# Colors
red = {0: lib.darkest_red
, 1: lib.darker_red
, 2: lib.dark_red
, 3: lib.red
, 4: lib.light_red
, 5: lib.lighter_red
, 6: lib.lightest_red}                    
