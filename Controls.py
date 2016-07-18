import libtcodpy as lib

def handle_keys(key, mouse, gamestate, player):

    # Alt + Enter to toggle fullscreen
    if key.vk == lib.KEY_ENTER and key.lalt:
        lib.console_set_fullscreen(not lib.console_is_fullscreen())
    # escape key to exit the game    
    elif key.vk == lib.KEY_ESCAPE:
        return 'exit game'

    # only 'hunting' if actively in a hunt -- turn based section
    if gamestate == 'hunting':
        if key.vk == lib.KEY_UP:
            player.move(0, -1)
            player.orientation = 'north'
        elif key.vk == lib.KEY_DOWN:
            player.move(0, 1)
            player.orientation = 'south'
        elif key.vk == lib.KEY_LEFT:
            player.move(-1, 0)
            player.orientation = 'west'
        elif key.vk == lib.KEY_RIGHT:
            player.move(1, 0)
            player.orientation = 'east'            

