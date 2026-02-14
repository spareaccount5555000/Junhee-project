import pygame
import random
pygame.init()

x = 864
y = 936
screen = pygame.display.set_mode((x,y))

bg = pygame.image.load("C:\Users\kiewj\Desktop\pro gd\flappybird\bg.png")
ground = pygame.image.load("C:\Users\kiewj\Desktop\pro gd\flappybird\ground.png")
pipe = pygame.image.load("C:\Users\kiewj\Desktop\pro gd\flappybird\pipe.png")
restart = pygame.image.load("C:\Users\kiewj\Desktop\pro gd\flappybird\restart.png")

ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
clock = pygame.time.Clock()

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
            img = pygame.image.load(f"C:\Users\kiewj\Desktop\pro gd\flappybird\bird{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.click = False
    def update(self):
        if flying == True:
            self.vel += 0.5
            if 8 < self.vel:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False
            flap_cooldown = 5
            self.counter += 1
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

bird_group = pygame.sprite.Group()
flappy = Bird(100, int(y/2))
bird_group.add(flappy)

while True:
    clock.tick(60)
    screen.blit(bg, (0,0))
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(ground, (ground_scroll, 768))
    if flappy.rect.bottom >= 768:
        game_over = True
        flying = False
        







