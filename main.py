import pygame

x = 800
y = 600

screen = pygame.display.set_mode((x, y))
border = pygame.Rect(x//2 - 5, 0, 10, y)
bg = pygame.image.load("spacebackground.png")
rockety = pygame.image.load("rocketyellow.png")
rockety1 = pygame.transform.rotate(pygame.transform.scale(rockety, (50, 40 )), -90)
rocketr = pygame.image.load("rocketred.png")
rocketr1 = pygame.transform.rotate(pygame.transform.scale(rocketr, (50, 40 )), 90)
vel = 0.3

def draw():
    screen.blit(bg, (0, 0))
    screen.blit(rocketr1, (150, 300))
    screen.blit(rockety1, (650, 300))
    pygame.display.update()

def redmove(keys_press, red):
    if keys_press[pygame.K_a] and red.x - vel > 0:
        red.x -= vel
    if keys_press[pygame.K_d] and red.x - vel < 400:
        red.x += vel
    if keys_press[pygame.K_w] and red.y - vel > 0:
        red.y -= vel
    if keys_press[pygame.K_s] and red.y - vel < 600:
        red.y += vel

def yellowmove(keys_press, yellow):
    if keys_press[pygame.K_LEFT] and yellow.x - vel > 400:
        yellow.x -= vel
    if keys_press[pygame.K_RIGHT] and yellow.x - vel < 800:
        yellow.x += vel
    if keys_press[pygame.K_UP] and yellow.y - vel > 0:
        yellow.y -= vel
    if keys_press[pygame.K_DOWN] and yellow.y - vel < 600:
        yellow.y += vel

run = True
red = pygame.Rect(150, 300, 50, 40)
yellow = pygame.Rect(650, 300, 50, 40)

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            pygame.quit()
    draw()
    keys_press = pygame.key.get_pressed()
    redmove(keys_press, red)
    yellowmove(keys_press, yellow)