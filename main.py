import pygame
import random
import time
pygame.init()

w = 900
h = 700

screen = pygame.display.set_mode((w, h))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\recycle\\bin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()

class Recycle(pygame.sprite.Sprite):
     def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\recycle\\" + img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

class Nonrecycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\recycle\\plasticbag.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

def changebackground(img):
    bg1 = pygame.image.load("C:\\Users\\kiewj\\Desktop\\pro gd\\recycle\\" + img)
    bg = pygame.transform.scale(bg1, (w, h))
    screen.blit(bg, (0, 0))

images = ["item1.png", "box.png", "pencil.png"]
item_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
plastic = pygame.sprite.Group()

for i in range(50):
    item = Recycle(random.choice(images))
    item.rect.x = random.randint(0, w)
    item.rect.y = random.randint(0, h)
    item_list.add(item)
    all_sprites.add(item)

for i in range(20):
    item = Nonrecycle()
    item.rect.x = random.randint(0, w)
    item.rect.y = random.randint(0, h)
    plastic.add(item)
    all_sprites.add(item)

bin = Bin()
all_sprites.add(bin)

run = True
score = 0
clock = pygame.time.Clock()
start_time = time.time()
font = pygame.font.SysFont("Arial", 18)
pygame.font.init()
text = font.render("Score: " + str(score),True, "Black")

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    time_elapsed = time.time() - start_time
    if time_elapsed >= 60 or score >= 20:
        if score >= 20:
            text = font.render("You Win, Well Done!", True, "Black")
            changebackground("youwin.jpg")
        else:
            text = font.render("You lost, Try again", True, "Black")
            changebackground("youlose.jpg")
        screen.blit(text, (150, 100))
    else:
        changebackground("background.png")
        countdown = font.render("Time left:" + str(60 - int(time_elapsed)), True, "Black")
        screen.blit(countdown, (10, 10))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y -= 5
        if keys[pygame.K_DOWN]:
            if bin.rect.y < h:
                bin.rect.y += 5
        if keys[pygame.K_LEFT]:
            if bin.rect.x > 0:
                bin.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x < w:
                bin.rect.x += 5
        item_hit = pygame.sprite.spritecollide(bin, item_list, True)
        plastic_hit = pygame.sprite.spritecollide(bin, plastic, True)
        for i in item_hit:
            score += 1
            text = font.render("Score: " + str(score), True, "Black")
        for i in plastic_hit:
            score -= 5
            text = font.render("Score: " + str(score), True, "Black")
        screen.blit(text, (10, 50))
        all_sprites.draw(screen)
    pygame.display.update()















