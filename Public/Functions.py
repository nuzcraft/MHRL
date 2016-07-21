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

# renders the backgrounds cons and basic border
def render_backgrounds(framecount):
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

    # this section is for the climbing vines
    lib.console_set_default_foreground(pv.main_con, lib.green)
    for f in range(framecount):
        lib.console_put_char(pv.main_con, 0, pv.MAIN_CON_HEIGHT - 1 - (f / 10), '|')       