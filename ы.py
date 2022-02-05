from msvcrt import LK_LOCK
import pygame
pygame.init()
import random
win = pygame.display.set_mode((500, 500))
win.fill((100, 100, 100))

clock = pygame.time.Clock()
class Circle:
    def __init__(self, x, y, rad, col, dir):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col
        self.dir = dir
    def draw(self, win):
        pygame.draw.circle(win, self.col, (self.x, self.y), self.rad)
    def move(self):
        if self.dir == 'right':
            self.x += 1
            if self.x > 500:
                self.dir ='left'
        else:
            self.x -=1
            if self.x < 0:
                self.dir = 'right'
list_circles = []
for i in range(0, 500, 1):
    list_circles.append(Circle(i*10, i*5, 30, random.choices(range(256), k=3), 'right'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((100, 100, 100))
    for i in range(100):
        list_circles[i].move()
        list_circles[i].draw(win)
    pygame.display.update()
