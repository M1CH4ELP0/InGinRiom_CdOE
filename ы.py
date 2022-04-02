import pygame as pg
import random
pg.init()
W, H, fps = 500, 500, 120
size = (W, H)
clock = pg.time.Clock()

pg.init()
win = pg.display.set_mode(size)

class Circle:
    def __init__(self, x, y, rad):
    def move(self):
    def show(self):
circles = []
for i in range(100):
    circles.append(Circle(W // 2, H // 2, 50))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    for circle in circles:
        circle.move()
    win.fill(225, 225, 225)
    for circle in circles:
        circle.show
    pg.display.update()
    clock.tick(fps)