import pygame
x = 800
y = 600

pygame.init()
screen = pygame.display.set_mode((x,y))
candycrush = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\matchthelogo\\candycrush.jpg")
ludo = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\matchthelogo\\ludo.jpg")
subwaysurfers = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\matchthelogo\\subwaysurfers.jpg")
templerun = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\matchthelogo\\templerun.jpg")

candycrush1 = pygame.transform.scale(candycrush, (100,100))
ludo1 = pygame.transform.scale(ludo, (100,100))
subwaysurfers1 = pygame.transform.scale(subwaysurfers, (100,100))
templerun1 = pygame.transform.scale(templerun, (100,100))

screen.blit(candycrush1, (550,80))
screen.blit(ludo1, (550,200))
screen.blit(subwaysurfers1, (550,320))
screen.blit(templerun1, (550,440))

font = pygame.font.SysFont("Bungee", 24)
textcandycrush = font.render("candy crush",True, "white")
textludo = font.render("ludo",True, "white")
textsubwaysurfers = font.render("subway surfers",True, "white")
texttemplerun = font.render("templerun",True, "white")

screen.blit(textcandycrush, (280, 320))
screen.blit(textludo, (280, 80))
screen.blit(textsubwaysurfers, (280, 200))
screen.blit(texttemplerun, (280, 440))

while True:
    pygame.display.update()
    event = pygame.event.poll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousepos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, "white", mousepos, 8)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        mousepos1 = pygame.mouse.get_pos()
        pygame.draw.line(screen, "white", mousepos, mousepos1)
        pygame.draw.circle(screen, "white", mousepos1, 8)
        pygame.display.update()


        




