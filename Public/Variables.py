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
dbl_pipes_corner_tr = chr(187)
dbl_pipes_corner_br = chr(188)
dbl_pipes_corner_tl = chr(201)
dbl_pipes_corner_bl = chr(200)
dbl_pipes_T_r = chr(204)
dbl_pipes_T_d = chr(203)
dbl_pipes_T_u = chr(202)
dbl_pipes_T_l = chr(185)
dbl_pipes_X = chr(206)

centered_dot = chr(249)
dbl_squiggly_equals = chr(247)

omega = chr(234)

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
LIMIT_FPS = 20

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
red = {
0: lib.darkest_red
, 1: lib.darker_red
, 2: lib.dark_red
, 3: lib.red
, 4: lib.light_red
, 5: lib.lighter_red
, 6: lib.lightest_red}

brown = {
0: lib.Color(26, 20, 13)
, 1: lib.Color(51, 41, 26)
, 2: lib.Color(77, 61, 38)
, 3: lib.Color(102, 82, 51)
, 4: lib.Color(128, 102, 64)
, 5: lib.Color(158, 134, 100)   
, 6: lib.Color(191, 171, 149)
, 7: lib.Color(222, 211, 195)      
}

# Border vines and flowers
# Flower
border_flower_char_l = [' ' + solid_u_arrow + centered_dot
                    , solid_l_arrow + omega + solid_r_arrow
                    , ' ' + solid_d_arrow + centered_dot]

border_flower_char_r = [centered_dot + solid_u_arrow + ' '
                    , solid_l_arrow + omega + solid_r_arrow
                    , centered_dot + solid_d_arrow + ' ']                    

border_flower_fore_color = {(0, 0): lib.green, (0, 1): lib.pink, (0, 2): lib.green
, (1, 0): lib.pink, (1, 1): lib.yellow, (1, 2): lib.pink
, (2, 0): lib.green, (2, 1): lib.pink, (2, 2): lib.green}

border_flowerbud_char = [' ' + centered_dot + ' '
                       , centered_dot + omega + centered_dot
                       , ' ' + centered_dot + ' ']                       

# Vine
border_vine_status_con_l = [
'  '
, '  '
, '  '
, '\\ '
, '  '
, '/ '
, '/' + dbl_squiggly_equals
, '\\\\'
, '//'
, '\\ '
, '\\\\'
, '\\/' 
, '  '
, '  ' 
, '  '      
]

border_vine_main_con_l = [
'  '
, '  '
, '  '
, '  '
, '  '
, '/ '
, '/ '
, '/ '
, '/ '
, '/ '
, '  '
, ' \\'
, ' /'
, '  '
, '\\' + dbl_squiggly_equals
, '\\ '
, '\\ '
, '\\ '
, '  '
, '\\ '
, '\\' + dbl_squiggly_equals
, '\\ '
, '  '
, '/ '
, '/ '
, '/ '
, '  '
, ' \\'
, ' /'
, '/ '
, '  '
, '/' + dbl_squiggly_equals
, '/ '
, '/ '
, '/ '
, '/ '
, '/ '
, '/ '
, '  '
, ' \\'
, '//'
, '/ '
, '\\' + dbl_squiggly_equals
, '\\ '
, '\\ '
, '\\ '
, '  '
, '\\ '
, '\\ '
, '\\ '
, '  '
, '/ '
, '/ '
, '/' + dbl_squiggly_equals
, '  '
, ' \\'
, ' /'
, '/ '
, '  '
, '/' + dbl_squiggly_equals
, '/' + dbl_squiggly_equals
, '/ '
, '  '
, '  '
, '  '
]

border_vine_status_con_r = [
'  '
, '  '
, '  '
, '  '
, dbl_squiggly_equals + '/'
, ' /'
, ' /'
, ' /'
, '  '
, ' /'
, dbl_squiggly_equals + '/'
, ' /'
, '  '
, ' \\'
, ' \\'
]

border_vine_main_con_r = [
' \\'
, '  '
, '/ '
, '\\/'
, dbl_squiggly_equals + '/'
, dbl_squiggly_equals + '/'
, '  '
, ' /'
, '/ '
, '\\ '
, '  '
, dbl_squiggly_equals + '/'
, ' /'
, ' /'
, '  '
, ' \\'
, ' \\'
, ' \\'
, '  '
, ' \\'
, ' \\'
, ' \\'
, dbl_squiggly_equals + '\\'
, ' /'
, '//'
, '\\ '
, '  '
, ' /'
, ' /'
, ' /'
, ' /'
, ' /'
, ' /'
, dbl_squiggly_equals + '/'
, '  '
, ' /'
, '/ '
, '\\ '
, '  '
, ' /'
, ' /'
, ' /'
, '  '
, ' \\'
, dbl_squiggly_equals + '\\'
, ' \\'
, '  '
, ' \\'
, ' \\'
, ' \\'
, dbl_squiggly_equals + '\\'
, '  '
, '/ '
, '\\ '
, '  '
, ' /'
, ' /'
, ' /'
, ' /'
, ' /'
, '  '
, '  '
, '  '
, '  '
, '  '
]

border_vine_map_con_l = [
 '  '
, '  '
, '  '
, ' \\'
, ' /'
, '  '
, '\\ '
, '\\ '
, '\\ '
, '  '
, '/ '
, '/' + dbl_squiggly_equals
, '/ '
, '  '
, '/ '
, '/ ' 
, '/ '
, '/' + dbl_squiggly_equals
, '/ '
, '  '
, '/ '
, '/ '
, '  '
, '  '
, '  '     
]

border_vine_menu_con_l = [
 '  '
, '  '
, '  '
, '  '
, '\\' + dbl_squiggly_equals
, '\\ '
, '\\ '
, '\\ '
, '  '
, '\\ '
, '\\' + dbl_squiggly_equals
, '\\ '
, '  '
, '/ '
, '/ '
, '/ ' 
, '  '
, ' \\'
, ' / '
, '/ '
, '  '
, '/' + dbl_squiggly_equals
, '/ '
, '/ '
, '/ ' 
, '/ '
, '/ '
, '/ '
, '  '
, ' \\'
, '//'
, '/ '
, '\\' + dbl_squiggly_equals
, '\\ '
, '\\ '
, '\\ '
, '  '
, '\\ '
, '\\ '
, '\\ '
, '  '
, '/ '
, '/ '
, '/' + dbl_squiggly_equals
, '  '
, ' \\'
, ' /'
, '/ '
, '  '
, '/' + dbl_squiggly_equals
, '/' + dbl_squiggly_equals
, '  '
, '  '
, '  '
, '  '
]

border_vine_map_con_r = [
 '  '
, '  '
, '  '
, dbl_squiggly_equals + '/'
, dbl_squiggly_equals + '/'
, '  '
, ' /'
, '/ '
, '\\ '
, '  '
, dbl_squiggly_equals + '/'
, ' /'
, ' /'
, '  '
, ' \\'
, ' \\' 
, ' \\'
, '  '
, ' \\'
, ' \\'
, ' \\'
, ' \\'
, '  '
, '  '
, '  '     
]

border_vine_menu_con_r = [
 '  '
, ' /'
, ' /'
, ' /'
, ' /'
, ' /'
, ' /'
, dbl_squiggly_equals + '/'
, '  '
, ' /'
, '/ '
, '\\ '
, '  '
, ' /'
, ' /'
, ' /' 
, '  '
, ' \\'
, dbl_squiggly_equals + '\\'
, '  '
, ' \\'
, ' \\'
, ' \\'
, dbl_squiggly_equals + '\\'
, '  ' 
, '/ '
, '\\ '
, '  '
, ' /'
, ' /'
, ' /'
, ' /'
, ' /'
, '  '
, ' /'
, '  '
, '  '
, dbl_squiggly_equals + '/'
, ' /'
, ' /'
, ' /'
, '  '
, ' /'
, dbl_squiggly_equals + '/'
, ' /'
, '  '
, ' \\'
, ' \\'
, ' \\'
, '  '
, '/ '
, '\\ '
, '  '
, '  '  
, '  '  
]
