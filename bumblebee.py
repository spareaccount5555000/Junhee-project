import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

bee = Actor("bee")
bee.pos = 300, 250

flower = Actor("flwr")
flower.pos = 165, 200

def draw():
    screen.blit("bckgrnd", (0, 0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score:" + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Time's up! Your final score is " + str(score),
        midtop=(WIDTH/2, 10), fontsize=40, color="red")

def place_flower():
    flower.x = randint(20, (WIDTH - 20))
    flower.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        bee.x = bee.x-2
    if keyboard.right:
        bee.x = bee.x--2

    if keyboard.up:
        bee.y = bee.y-2
    if keyboard.down:
        bee.y = bee.y--2

    flower_collected = bee.colliderect(flower)

    if flower_collected:
        score = score+10
        place_flower()


clock.schedule(time_up, 25.0)

pgzrun.go()




