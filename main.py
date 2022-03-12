import pygame as pg
import random
pg.init()
W, H, fps = 1920, 1080, 120
size = (W, H)
clock = pg.time.Clock()

pg.init()
win = pg.display.set_mode(size)

def load_img(name):
    img = pg.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img
class Spr(pg.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_img("t.png")
        self.image = image = pg.transform.scale(self.image, (500, 250))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W)
        self.rect.y = random.randrange(H)
    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
img1 = pg.image.load("h.jpg")
all_sprites = pg.sprite.Group()
for i in range(2):
    Spr(all_sprites)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    all_sprites.update()
    win.fill((225, 225, 225))
    win.blit(img1, (0, 0))
    all_sprites.draw(win)
    pg.display.update()
    clock.tick(fps)