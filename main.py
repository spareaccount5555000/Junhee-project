import pygame
import time
pygame.init()

x = 515
y = 800

screen = pygame.display.set_mode((x, y))

pygame.display.set_caption("Christmas card")

img1pre = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\christmascard\\christmastree.jpg")
img1 = pygame.transform.scale(img1pre, (515, 800))


while True:
    font = pygame.font.SysFont("TimesNewRoman", 24)
    text = font.render("Wish you a merry Chirstmas", True, "black")
    screen.fill("gray")
    screen.blit(img1, (0, 0))
    screen.blit(text, (0, 0))
    pygame.display.update()
    time.sleep(3)
    img2pre = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\christmascard\\chirstmas2.jpg")
    img2 = pygame.transform.scale(img2pre, (515, 800))
    text2 = font.render("and a happy new year", True, "black")
    screen.blit(img2, (0, 0))
    screen.blit(text2, (0, 0))
    pygame.display.update()
    time.sleep(3)



