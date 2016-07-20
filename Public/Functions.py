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

# renders the backgrounds cons
def render_backgrounds():
    # main con
    lib.console_set_default_background(pv.main_con, pv.red[0])
    lib.console_rect(pv.main_con, 0, 0, pv.MAIN_CON_WIDTH, pv.MAIN_CON_HEIGHT, False, lib.BKGND_SET)
    for x in range(3, pv.MAIN_CON_WIDTH - 3):
        lib.console_put_char_ex(pv.main_con, x, pv.MAIN_CON_HEIGHT - 1, pv.dbl_pipes_horiz, lib.green, lib.BKGND_SET)
        lib.console_put_char_ex(pv.main_con, x, 0, pv.dbl_pipes_horiz, lib.green, lib.BKGND_SET)
    # lib.console_put_char_ex(pv.main_con, 5, 0, pv.dbl_pipes_horiz, lib.blue, lib.BKGND_SET)
    # status con
    lib.console_set_default_background(pv.status_con, lib.sepia)
    lib.console_rect(pv.status_con, 0, 0, pv.STATUS_CON_WIDTH, pv.STATUS_CON_HEIGHT, False, lib.BKGND_SET)
    # map con
    lib.console_set_default_background(pv.map_con, lib.light_sepia)
    lib.console_rect(pv.map_con, 0, 0, pv.MAP_CON_WIDTH, pv.MAP_CON_HEIGHT, False, lib.BKGND_SET)
    # menu_con
    lib.console_set_default_background(pv.menu_con, lib.lighter_sepia)
    lib.console_rect(pv.menu_con, 0, 0, pv.MENU_CON_WIDTH, pv.MENU_CON_HEIGHT, False, lib.BKGND_SET)
