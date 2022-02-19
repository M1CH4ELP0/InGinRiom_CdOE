import pygame as pg
import random
pg.init()
win = pg.display.set_mode((500, 500))
win.fill((0, 0, 0))

cross = '#046582'
circle = '#e4bad4'
class Board:
    def __init__(self, W, H, size):
        self.w, self.h = W, H
        self.size = size
        self.board = [
            [0, 0, 0]
            [0, 0, 0]
            [0, 0, 0]
        ]
        self.move = 1
    def click(self,mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        self.board[y][x] = self.move
        self.move = -self.move
    def render(self, screen):
        
        
        
    

board = Board(600, 600, 200)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)
    screen.fill(255, 255, 255)
    board.render(screen)
    pg.display.update()
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        pg.quit()
        exit
