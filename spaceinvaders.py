import pygame
pygame.font.init()
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
bulletvel = 0.5
maxbullets = 3
yellowhit = pygame.USEREVENT+1
redhit = pygame.USEREVENT+2 
font = pygame.font.SysFont("Times New Roman", 24)
fps = 165

def drawing(red, yellow, redbullets, yellowbullets, redhealth, yellowhealth):
    yellow = "yellow"
    red = "red"
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, "black", border)
    screen.blit(rocketr1, (150, 300))
    screen.blit(rockety1, (650, 300))
    redhealthtext = font.render("health: " + str(redhealth), True, "black")
    yellowhealthtext = font.render("health: " + str(yellowhealth), True, "black")
    screen.blit(redhealthtext, (50, 50))
    screen.blit(yellowhealthtext, (750, 50))
    for i in redbullets:
        pygame.draw.rect(screen, red, i)
    for i in yellowbullets:
        pygame.draw.rect(screen, yellow, i)
    pygame.display.update()

def handlebullets(redbullets, yellowbullets, red, yellow):
    for i in redbullets:
        i.x -= bulletvel
        if yellow.colliderect(i):
            pygame.event.post(pygame.event.Event(yellowhit))
            redbullets.remove(i)
        elif i.x < 0:
            redbullets.remove(i)
    for i in yellowbullets:
        i.x -= bulletvel
        if red.colliderect(i):
            pygame.event.post(pygame.event.Event(redhit))
            yellowbullets.remove(i)
        elif i.x < 0:
            yellowbullets.remove(i)

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
redbullets = []
yellowbullets = [] 
redhealth = 10
yellowhealth = 10
clock = pygame.time.Clock()

while run:
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            pygame.quit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LCTRL and len(yellowbullets) < maxbullets:
                bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                yellowbullets.append(bullet)
            if i.key == pygame.K_RCTRL and len(redbullets) < maxbullets:
                bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                redbullets.append(bullet)
        if i.type == redhit:
            redhealth -= 1
        if i.type == yellowhit:
            yellowhealth -= 1
    keys_press = pygame.key.get_pressed()
    redmove(keys_press, red)
    yellowmove(keys_press, yellow)
    handlebullets(redbullets, yellowbullets, red, yellow)
    drawing(red, yellow, redbullets, yellowbullets, redhealth, yellowhealth)
