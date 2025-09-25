from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

character = load_image('animation_sheet.png')

running = True
frame = 0

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    pass

close_canvas()