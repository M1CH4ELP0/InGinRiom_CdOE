import pygame as pg
import random
pg.init()
win = pg.display.set_mode((500, 500))
win.fill((0, 0, 0))
class Star:
    def __init__(self, pressed):
        self.x = pressed[0]
        self.y = pressed[1]
        self.obj = 'rect'
    def draw(self,win, fig):
        self.obj = fig
        if self.obj == 'circle':
            pg.draw.circle(win, ((random.choices(range(0, 256), k=3))), pg.mouse.get_pos(), 30)
        elif self.obj == 'rect':
            pg.draw.rect(win, ((random.choices(range(256), k=3))), (self.x, self.y, 100, 150))
    

            
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    a = Star
    pressed = pg.mouse.get_pressed()
    keys = pg.key.get_pressed()
    if pressed[0]:
        pos = pg.mouse.get_pos()
        a = Star(pos)
        #qqqa.draw(win)
        if keys[pg.K_w]:
            a.draw(win,'circle')
        if keys[pg.K_q]:
            a.draw(win, 'rect')
    if keys[pg.K_SPACE]:
        win.fill((0, 0, 0))
        
    pg.display.update()