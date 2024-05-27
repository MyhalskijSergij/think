import pygame
pegame.init ()
WIDTH, HEIGHT = 780, 580
win = pygame.display.set_mode((WIDTH, HEITGHT))
pygame.display.set_caption("Моя гра")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ryning = False
pygame.quit()