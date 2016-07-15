
import libtcodpy as lib
import Classes.Object as obj

# size of the WindowsError
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

# size of the map
MAP_WIDTH = 80
MAP_HEIGHT = 40

# FPS Limit
LIMIT_FPS = 20

# Current Version
Version = '0.1'

# initialization
lib.console_set_custom_font('cp437_8x8.png', lib.FONT_LAYOUT_ASCII_INROW)
lib.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'MHRL ' + Version, False)
lib.sys_set_fps(LIMIT_FPS)

# create a new console
con = lib.console_new(MAP_WIDTH, MAP_HEIGHT)
lib.console_set_default_background(con, lib.black)

# create the player object
player = obj.Object(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, '@', 'player', lib.white)

while not lib.console_is_window_closed():

    key = lib.Key()
    mouse = lib.Mouse()

    lib.sys_check_for_event(lib.EVENT_KEY_PRESS | lib.EVENT_MOUSE, key, mouse)

    player.draw(con)

    lib.console_blit(con, 0, 0, MAP_WIDTH, MAP_HEIGHT, 0, 0, 0)
    lib.console_flush()

    if key.vk == lib.KEY_ESCAPE:
        break