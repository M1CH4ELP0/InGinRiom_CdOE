import pygame as pg
import random
pg.init()
win = pg.display.set_mode((500, 500))
win.fill((0, 0, 0))
W, H = 600, 600
screen = pg.display.set_mode((W, H))
size = 30
cross = '#046582'
circle = '#e4bad4'
def draw_circle(sc, x, y, size):
    x = (x + .5) * size
    y = (y + .5) * size
    pg.draw.circle(sc,circle, (x, y), (size-3) // 2, 3)
def draw_cross(sc, x, y, size):
    x = x * size + 3
    y = y * size + 3
    pg.draw.line(sc,cross, (x, y), (x + size-3, y + size - 3), 3)
    pg.draw.line(sc,cross, (x+ size - 3, y - 3), (x,y + size - 3), 3)
class Board:
    def __init__(self, W, H, size):
        self.w, self.h = W, H
        self.size = size
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.move = 1
    def click(self,mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        self.board[y][x] = self.move
        self.move = -self.move
    def render(self, screen):
        pg.draw.line(screen, (0, 0, 0), (0, 200), (self.w, 200))
        pg.draw.line(screen, (0, 0, 0), (0, 400), (self.w, 400))
        pg.draw.line(screen, (0, 0, 0), (200, 0), (200, self.h))
        pg.draw.line(screen, (0, 0, 0), (400, 0), (400, self.h))
        for x in range(3):
            for y in range(3):
                if self.board[y][x] == 1:
                    draw_cross(screen, x, y, self.size)
                elif self.board[y][x] == -1:
                    draw_circle(screen, x, y, self.size)
        
        
    

board = Board(W, H, 200)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)
    screen.fill((255, 255, 255))
    board.render(screen)
    pg.display.update()
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        pg.quit()
        exit
    
        