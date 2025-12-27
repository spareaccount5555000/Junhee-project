import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))

rocket = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\rocketgame\\rocket.png")
bg = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\rocketgame\\space.jpg")

keys = [False, False, False, False]

rocketx = 400
rockety = 300

while rockety < 600:
    screen.blit(bg, (0, 0))
    screen.blit(rocket, (rocketx, rockety))
    pygame.display.flip()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == K_UP:
                keys[0] = True
            if i.key == K_DOWN:
                keys[1] = True
            if i.key == K_LEFT:
                keys[2] = True
            if i.key == K_RIGHT:
                keys[3] = True
        if i.type == pygame.KEYUP:
            if i.key == K_UP:
                keys[0] = False
            if i.key == K_DOWN:
                keys[1] = False
            if i.key == K_LEFT:
                keys[2] = False
            if i.key == K_RIGHT:
                keys[3] = False
    if keys[0]:
        if rockety > 0:
            rockety -= 0.3
    if keys[1]:
        if rockety < 600:
            rockety += 0.3
    if keys[2]:
        if rocketx > 0:
            rocketx -= 0.3
    if keys[3]:
        if rocketx < 800:
            rocketx += 0.3
    
    rockety += 0.2
    
    



