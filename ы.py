import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
win.fill((100, 100, 100))
FPS = 60
clock = pygame.time.Clock()
class Circle:
    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col
    def draw(self, win):
        pygame.draw.circle(win, self.col, (self.x, self.y), self.rad)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x-=10
        elif keys[pygame.K_RIGHT]:
            self.x += 10
        elif keys[pygame.K_UP]:
            self.y-= 10
        elif keys[pygame.K_DOWN]:
            self.y+= 10
    def upd(self):
        pygame.display.update()
        win.fill((100, 100, 100))
a= Circle(250, 250, 50, 'yellow')
a.draw(win)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    a.move()
    a.draw(win)
    a.upd()
    clock.tick(FPS)