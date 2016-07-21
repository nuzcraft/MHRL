
import libtcodpy as lib
import Controls as controls
import Classes.Object as obj
import Public.Variables as pv
import Public.Functions as pf

# initialization
lib.console_set_custom_font('cp437_8x8.png', lib.FONT_LAYOUT_ASCII_INROW)
lib.console_init_root(pv.SCREEN_WIDTH, pv.SCREEN_HEIGHT, 'MHRL ' + pv.Version, False)
lib.sys_set_fps(pv.LIMIT_FPS)

# create the player object
player = obj.Object(pv.SCREEN_WIDTH / 2, pv.SCREEN_HEIGHT / 2, pv.player_greatsword_char, 'player', lib.white, 'east')

player2 = obj.Object(pv.SCREEN_WIDTH / 2 + 5, pv.SCREEN_HEIGHT / 2, pv.player_greatsword_char, 'player', lib.blue, 'west')

gamestate = 'hunting' # used to indicate when on a hunt

framecount = 0

while not lib.console_is_window_closed():

    lib.sys_check_for_event(lib.EVENT_KEY_PRESS | lib.EVENT_MOUSE, pv.key, pv.mouse)

    pf.render_backgrounds(framecount)

    player.draw(pv.main_con)
    player2.draw(pv.main_con)

    lib.console_blit(pv.main_con, 0, 0, pv.MAIN_CON_WIDTH, pv.MAIN_CON_HEIGHT, 0, 0, pv.MAIN_CON_Y)
    lib.console_blit(pv.status_con, 0, 0, pv.STATUS_CON_WIDTH, pv.STATUS_CON_HEIGHT, 0, 0, 0)
    lib.console_blit(pv.map_con, 0, 0, pv.MAP_CON_WIDTH, pv.MAP_CON_HEIGHT, 0, pv.MAP_CON_X, 0)
    lib.console_blit(pv.menu_con, 0, 0, pv.MENU_CON_WIDTH, pv.MENU_CON_HEIGHT, 0, pv.MENU_CON_X, pv.MENU_CON_Y)
    lib.console_flush()

    player.clear(pv.main_con)

    player_action = controls.handle_keys(pv.key, pv.mouse, gamestate, player)

    framecount += 1
    print framecount
    if framecount == 1000:
        framecount = 0

    if player_action == 'exit game':
        break
