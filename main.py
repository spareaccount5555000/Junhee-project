import pgzrun
import random

HEIGHT = 600
WIDTH = 800
GRAVITY = 2000

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 50
        self.vy = 0
        self.r = 20
    
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle( pos, self.r, "blue")

ball1 = Ball(400, 300)

def draw():
    screen.clear()
    ball1.draw()

def update(dt):
    uy = ball1.vy
    ball1.vy += GRAVITY * dt
    ball1.y += (uy + ball1.vy) * 0.5 * dt

    if ball1.y > HEIGHT - ball1.r:
        ball1.y = HEIGHT - ball1.r
        ball1.vy = -ball1.vy * 0.5
    
    ball1.x += ball1.vx * dt

    if ball1.x > WIDTH - ball1.r or ball1.x < ball1.r:
        ball1.vx = -ball1.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball1.vy = -400

pgzrun.go()




    




        
        