
import libtcodpy as lib
import Classes.Object as obj
import Public.Variables as pv

# initialization
lib.console_set_custom_font('cp437_8x8.png', lib.FONT_LAYOUT_ASCII_INROW)
lib.console_init_root(pv.SCREEN_WIDTH, pv.SCREEN_HEIGHT, 'MHRL ' + pv.Version, False)
lib.sys_set_fps(pv.LIMIT_FPS)

# create a new console
con = lib.console_new(pv.MAP_WIDTH, pv.MAP_HEIGHT)
lib.console_set_default_background(con, lib.black)

# create the player object
player = obj.Object(pv.SCREEN_WIDTH / 2, pv.SCREEN_HEIGHT / 2, pv.player_greatsword_char, 'player', lib.white, 'east')

player2 = obj.Object(pv.SCREEN_WIDTH / 2 + 5, pv.SCREEN_HEIGHT / 2, pv.player_greatsword_char, 'player', lib.blue, 'west')

while not lib.console_is_window_closed():

    key = lib.Key()
    mouse = lib.Mouse()

    lib.sys_check_for_event(lib.EVENT_KEY_PRESS | lib.EVENT_MOUSE, key, mouse)

    player.draw(con)
    player2.draw(con)

    lib.console_blit(con, 0, 0, pv.MAP_WIDTH, pv.MAP_HEIGHT, 0, 0, 0)
    lib.console_flush()

    if key.vk == lib.KEY_ESCAPE:
        break
