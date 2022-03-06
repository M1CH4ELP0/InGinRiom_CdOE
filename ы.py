import pygame as pg

pg.init()
size = W, H = 1920, 1080
fps = 30
win = pg.display.set_mode(size)
def l(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img


img = pg.image.load('400px-Vexillum_Ucrainae.svg.png')
img1 = pg.transform.scale(img, (200, 200))
img2 = pg.transform.scale(img, (700, 200))
im = pg.image.load('f.jpg')
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    win.blit(img1, (500, 0))
    win.blit(img2, (700, 0))
    win.blit(im, (200, 200))
    pg.display.update()