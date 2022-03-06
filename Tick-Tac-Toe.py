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
    def check(self):
        end_info = end(self.board)
        shift = self.w // 10
        if end_info is not None:
            type_end = end_info[0]
            num = end_info[1]
            if type_end == 'col':
                x0, y0 = (num + .5) * self.size, shift
                x1, y1 = (num + .5) * self.size, self.size * 3 - shift
            elif type_end == 'line':
                x0, y0 = shift, (num + .5) * self.size
                x1, y1 = 3 * self.size - shift, (num + .5) * self.size
            elif type_end == 'diag':
                if num == 1:
                    x0, y0 = shift ,shift
                    x1, y1 = 3 * self.size - shift, 3 * self.size - shift
                else:
                    x0, y0 = 3 * self.size - shift, shift
                    x1, y1 = shift, 3 * self.size - shift
            pg.draw.line(screen, (225, 0, 0), (x0, y0), (x1, y1), 10)
            pg.display.update()
            pg.time.delay(3000)
            return True
        else:
            return False
def check_i_col(x, i):
    if x[0][i] == x[1][i] == x[2][i] != 0:
        return True
    else:
        return False
def check_i_line(x, i):
    if x[i][0] == x[i][1] == x[i][2] != 0:
        return True
    else:
        return False
def check_secondary_diag(x):
    if x[0][0] == x[1][1] == x[2][2] != 0:
        return True
    else:
        return False
def check_main_diag(x):
    if x[2][0] == x[1][1] == x[0][2] != 0:
        return True
    else:
        return False
def end(board):
    for i in range(3):
        if check_i_col(board, i):
            return 'col' , i
        if check_i_line(board, i):
            return 'line', i
    if check_main_diag(board):
        return 'diag', 2
    if check_secondary_diag(board):
        return 'diag', 1
    return None
    
board = Board(W, H, 200)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)
    screen.fill((255, 255, 255))
    board.render(screen)
    pg.display.update()
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE] or board.check():
        pg.quit()
        exit()