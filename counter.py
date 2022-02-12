import posixpath
import pygame as pg
import random
pg.init()
win = pg.display.set_mode((500, 500))
win.fill((0, 0, 0))
class Star:
    def __init__(self, pressed):
        self.x = pressed[0]
        self.y = pressed[1]
    def draw(self, win):
        pg.draw.circle(win,(random.choices(range(256), k=3)), (self.x, self.y), 30)

            
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    a = Star
    pressed = pg.mouse.get_pressed()
    if pressed[0]:
        pos = pg.mouse.get_pos()
        a = Star(pos)
        a.draw(win)
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        win.fill((0, 0, 0))
    if keys[pg.K_q]:
        
    
    pg.display.update()