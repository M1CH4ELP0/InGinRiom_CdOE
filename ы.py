import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 250
y = 250



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    z=3

    win.fill((225, 225, 220))
    pygame.draw.circle(win, (225, 225, 0), (x, y), 50)

    if x <= 150:
        pygame.draw.circle(win, (225, 0, 0), (x, y), 50)
        z-=2
    elif y<= 150:
        pygame.draw.circle(win, (225, 0, 0), (x, y), 50)
        z-=2
    elif x >= 400:
        pygame.draw.circle(win, (225, 0, 0), (x, y), 50)
        z-=2
    elif y>= 400:
        pygame.draw.circle(win, (225, 0, 0), (x, y), 50)
        z-=2

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=z
    elif keys[pygame.K_RIGHT]:
        x += z
    elif keys[pygame.K_UP]:
        y-= z
    elif keys[pygame.K_DOWN]:
        y+= z
    else:
        if x> 250:
            x-=1
        if x<250:
            x+=1
        if y<250:
            y+=1
        if y>250:
            y-=1
    pygame.display.update()

    pygame.time.delay(10)