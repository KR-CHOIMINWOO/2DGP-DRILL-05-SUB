from pico2d import *

from move_character_with_mouse import handle_events

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running , dir_x, dir_y, z
    events = get_events()

    pass

running = True
frame = 0
x = 1280 // 2
y = 1024 // 2
z = 0
dir_x = 0
dir_y = 0

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * z, 100, 100, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)
    pass

close_canvas()