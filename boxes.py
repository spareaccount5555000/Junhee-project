import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600

def draw():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    width = WIDTH - 300
    height = HEIGHT - 500

    for i in range(20):
        rect = Rect((0,0),(width, height))
        rect.center = 300, 300
        screen.draw.rect(rect, (r, g, b))

        width -= 30
        height += 30
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)


pgzrun.go()
