import pygame
import sys 
import math

from factory import create_objects

from space.space_gameloop import space_gameloop
from game_over.game_over_gameloop import game_over_gameloop
from planet_1.planet_1_gameloop import planet_1_gameloop




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

    match(stage):
        case "space":
            stage = space_gameloop(space_objects, keys, screen, font, stage)
        case "game_over":
            stage = game_over_gameloop(space_objects, keys, screen, font)
        case "planet_1":
            stage = planet_1_gameloop(space_objects, keys, screen, font)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
