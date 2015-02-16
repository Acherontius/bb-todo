#The File
import libtcodpy as tcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20

def handle_keys():
    key = tcod.console_wait_for_keypress(True)

    if key.vk == tcod.KEY_ESCAPE:
        return True

tcod.console_set_custom_font('terminal.png', tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_ASCII_INCOL)

tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'bb-todo', False)

tcod.sys_set_fps(LIMIT_FPS)

while not tcod.console_is_window_closed():
    tcod.console_set_default_foreground(0, tcod.white)
    tcod.console_put_char(0, 1, 1, '@', tcod.BKGND_NONE)
    tcod.console_flush()

    exit = handle_keys()
    if exit:
        tcod.console_delete(0)
        break
