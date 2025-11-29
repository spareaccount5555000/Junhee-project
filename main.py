import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])

class Circle():
    def __init__(self, color, pos, r, w):
        self.color = color
        self.pos = pos
        self.r = r
        self.w = w
        self.screen = screen
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.r, self.w)
    
    def draw1(self, grow):
        self.r += grow
        pygame.draw.circle(self.screen, self.color, self.pos, self.r, self.w)

         


pos = (400, 300)
r = 30
w = 2
pygame.draw.circle(screen, "blue", pos, r, w)
pygame.display.update()

circle1 = Circle("blue", pos , 60, 2)
circle2 = Circle("white", pos , 90, 3)  
circle3 = Circle("purple", pos , 120, 4)    

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if i.type == pygame.MOUSEBUTTONDOWN:
            circle1.draw()
            circle2.draw()
            circle3.draw()
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            circle1.draw1(20)
            circle2.draw1(30)
            circle3.draw1(40)
            pygame.display.update()
        elif i.type == pygame.MOUSEMOTION:
            mpos = pygame.mouse.get_pos()
            circle4 = Circle("white", mpos , 4, 4)
            circle4.draw()
            pygame.display.update()


        
    

