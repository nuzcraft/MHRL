import sys
sys.path.append('..')
import libtcodpy as lib
import Public.Variables as pv


# get_center takes a length and width of a rectangle and returns the center tile
# only works on odd by odd things, if even, it will skew down for width and right for length
def get_center(length, width):
    x_center = round(length / 2)
    y_center = round(width / 2) 
    return (int(x_center), int(y_center))

# draw_char takes a character or set of characters and draws them to the specified console
def draw_char(con_x, con_y, char, console, fore_color_complex = None, fore_color_simple = lib.white, string = False):
    CHAR_HEIGHT = len(char)
    CHAR_WIDTH = len(char[0])
    # get the center of the character(s) so we can draw in the right place   
    for a in range(CHAR_HEIGHT):
        for b in range(CHAR_WIDTH):
            if char[a][b] != ' ':
                if fore_color_complex != None:
                    lib.console_set_default_foreground(console, fore_color_complex[(a, b)])
                else: 
                    lib.console_set_default_foreground(console, fore_color_simple)
                # because of the way lists are handled vs strings, the second clause handles a string input    
                if string == False:        
                    lib.console_put_char(console, con_x + b, con_y + a, char[a][b], lib.BKGND_NONE)
                else:
                    lib.console_put_char(console, con_x + a, con_y + b, char[a][b], lib.BKGND_NONE)    
   

# renders the backgrounds cons and basic border
def render_backgrounds():
    for (con, con_height, con_width) in [(pv.main_con, pv.MAIN_CON_HEIGHT, pv.MAIN_CON_WIDTH)
    , (pv.status_con, pv.STATUS_CON_HEIGHT, pv.STATUS_CON_WIDTH)
    , (pv.map_con, pv.MAP_CON_HEIGHT, pv.MAP_CON_WIDTH)
    , (pv.menu_con, pv.MENU_CON_HEIGHT, pv.MENU_CON_WIDTH)]:
        # set the background
        lib.console_set_default_background(con, pv.brown[0])
        lib.console_set_default_foreground(con, pv.brown[3])
        lib.console_rect(con, 0, 0, con_width, con_height, False, lib.BKGND_SET)
        # outer walls
        for x in range(3, con_width - 3):
            lib.console_put_char(con, x, con_height - 1, pv.dbl_pipes_horiz)
            lib.console_put_char(con, x, 0, pv.dbl_pipes_horiz)
        for y in range(3, con_height - 3):
            lib.console_put_char(con, 0, y, pv.dbl_pipes_vert)
            lib.console_put_char(con, con_width - 1, y, pv.dbl_pipes_vert)
        # corners    
        for x in (0, con_width - 1):
            for y in (0, con_height - 1):
                lib.console_put_char(con, x, y, pv.centered_dot)
        # fancy corner stuff
        # tl corner
        lib.console_put_char(con, 2, 0, pv.dbl_pipes_T_d)
        lib.console_put_char(con, 1, 0, pv.dbl_pipes_corner_tl)  
        lib.console_put_char(con, 0, 2, pv.dbl_pipes_T_r)
        lib.console_put_char(con, 0, 1, pv.dbl_pipes_corner_tl)
        lib.console_put_char(con, 2, 1, pv.dbl_pipes_corner_br) 
        lib.console_put_char(con, 1, 2, pv.dbl_pipes_corner_br)
        lib.console_put_char(con, 1, 1, pv.dbl_pipes_X)
        # tr corner
        lib.console_put_char(con, con_width - 3, 0, pv.dbl_pipes_T_d)
        lib.console_put_char(con, con_width - 2, 0, pv.dbl_pipes_corner_tr)
        lib.console_put_char(con, con_width - 1, 2, pv.dbl_pipes_T_l)
        lib.console_put_char(con, con_width - 1, 1, pv.dbl_pipes_corner_tr)
        lib.console_put_char(con, con_width - 3, 1, pv.dbl_pipes_corner_bl)
        lib.console_put_char(con, con_width - 2, 2, pv.dbl_pipes_corner_bl)
        lib.console_put_char(con, con_width - 2, 1, pv.dbl_pipes_X) 
        # bl corner
        lib.console_put_char(con, 2, con_height - 1, pv.dbl_pipes_T_u)
        lib.console_put_char(con, 1, con_height - 1, pv.dbl_pipes_corner_bl)  
        lib.console_put_char(con, 0, con_height - 3, pv.dbl_pipes_T_r)
        lib.console_put_char(con, 0, con_height - 2, pv.dbl_pipes_corner_bl)
        lib.console_put_char(con, 2, con_height - 2, pv.dbl_pipes_corner_tr) 
        lib.console_put_char(con, 1, con_height - 3, pv.dbl_pipes_corner_tr)
        lib.console_put_char(con, 1, con_height - 2, pv.dbl_pipes_X)  
        # br corner
        lib.console_put_char(con, con_width - 3, con_height - 1, pv.dbl_pipes_T_u)
        lib.console_put_char(con, con_width - 2, con_height - 1, pv.dbl_pipes_corner_br)  
        lib.console_put_char(con, con_width - 1, con_height - 3, pv.dbl_pipes_T_l)
        lib.console_put_char(con, con_width - 1, con_height - 2, pv.dbl_pipes_corner_br)
        lib.console_put_char(con, con_width - 3, con_height - 2, pv.dbl_pipes_corner_tl) 
        lib.console_put_char(con, con_width - 2, con_height - 3, pv.dbl_pipes_corner_tl)
        lib.console_put_char(con, con_width - 2, con_height - 2, pv.dbl_pipes_X)

def render_vines(framecountdiv10):
    # this section is for the climbing vines
    # the y_location moves up the con to simulate the climbing of the vine
    y_location = pv.SCREEN_HEIGHT - 1 - framecountdiv10
    main_y_location = y_location - pv.STATUS_CON_HEIGHT
    # draw the flowers
    if main_y_location >= 0:
        # this writes to the main con
        main_con_flower_location = [3, 21, 49]
        if main_y_location - 1 in main_con_flower_location:
            draw_char(0, main_y_location - 1, pv.border_flowerbud_char, pv.main_con, fore_color_simple = lib.green)
        if main_y_location in main_con_flower_location:
            draw_char(0, main_y_location, pv.border_flower_char_l, pv.main_con, pv.border_flower_fore_color)
        # draw the vines    
        draw_char(0, main_y_location, pv.border_vine_main_con_l[main_y_location], pv.main_con, fore_color_simple = lib.green, string = True)
    elif y_location >=0 :
        # this writes to the status con
        status_con_flower_location = [3]
        if y_location - 1 in status_con_flower_location:
            draw_char(0, y_location - 1, pv.border_flowerbud_char, pv.status_con, fore_color_simple = lib.green)
        if y_location in status_con_flower_location:
            draw_char(0, y_location, pv.border_flower_char_l, pv.status_con, pv.border_flower_fore_color)
        # draw the vines    
        draw_char(0, y_location, pv.border_vine_status_con_l[y_location], pv.status_con, fore_color_simple = lib.green, string = True)
