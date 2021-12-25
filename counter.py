import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 100
y = 150
y1 = 50
x1 = 250
dc= 0
dv = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if dc == 1:
        x=x-1
    elif dc == 0:
        x = x+1

    if x > 400:
        dc += 1
    if x <0:
        dc -= 1

    win.fill((225, 225, 225))
    pygame.draw.rect(win, (225, 225, 0), (x, y, 100, 150))

    if dv == 1:
        y1=y1-1
    elif dv == 0:
        y1 = y1+1

    if y1 > 450:
        dv+=1
    elif y1 < 50:
        dv-=1
        

    pygame.draw.circle(win, (155, 225, 45), (x1, y1), 50)
    pygame.display.update()

    pygame.time.delay(5)