import pygame
import sys 
import math

from space.factory import create_objects

from space.space_gameloop import space_gameloop



pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("PNG zeichnen")
font = pygame.font.Font("assets/8_bit_font.ttf", 18)
clock = pygame.time.Clock()


space_objects = create_objects(screen)
stage = "space"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Mit ESC beenden
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    if stage == "space":
        stage =space_gameloop(space_objects, keys, screen, font, stage)
    
    if stage == "planet_1":
        pass

    print(stage)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
