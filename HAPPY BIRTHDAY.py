import pygame as pg

pg.init()
win = pg.display.set_mode((500, 500))
win.fill((51, 64, 43))
W, H = 600, 600

f1 = pg.font.Font(None, 36)
text1 = f1.render('        С ДНЁМ РОЖДЕНИЯ, МАМА!!', 1, (41, 85, 255))

dog_surf = pg.image.load('io.png')
dog_rect = dog_surf.get_rect(
    bottomright=(500, 500))
win.blit(dog_surf, dog_rect)

win.blit(text1, (10, 50))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()

