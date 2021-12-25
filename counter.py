import pygame
pygame.init()
a = int(input())
d = int(input())
x = a / d
win = pygame.display.set_mode((a, a))
for f in range(0, a, 2):
    for i in range(0, a, 2):
        pygame.draw.rect(win, (225, 225, 225), (int(x*i), f * 50, int(x), int(x)))
        pygame.draw.rect(win, (225, 225, 225), (int(x*i+50), f * 50 + 50, int(x), int(x)))
pygame.display.update()
pygame.display.set_caption('aaaAAAaAAAAAaaa')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
