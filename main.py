import pgzrun
from random import randint

TITLE = "Good Shot"
WIDTH = 500
HEIGHT = 500

message = ""

alien = Actor('alien')

def draw():
    screen.clear()
    screen.fill(color = (204,229,255))

    alien.draw()
    screen.draw.text(message, center = (400,10), fontsize = 30)

def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, WIDTH-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "good shot"
        place_alien()
    else:
        message = "You missed"

place_alien()
pgzrun.go()
