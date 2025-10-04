import os
import sys
import pygame
import math

# Arbeitsverzeichnis auf das Verzeichnis dieser Datei setzen
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from factory import create_objects

from gameloops.space import SpaceGameloop
from gameloops.planet_1 import Planet1Gameloop
from gameloops.game_over import GameOverGameloop

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("PNG zeichnen")
font = pygame.font.Font("assets/8_bit_font.ttf", 18)
clock = pygame.time.Clock()

objects = create_objects(screen)

space_gameloop = SpaceGameloop(objects, font, screen)
planet1_gameloop = Planet1Gameloop(objects, font, screen)
gameover_gameloop = GameOverGameloop(objects, font, screen)

stage = "planet_1"
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

    match stage:
        case "space":
            stage = space_gameloop.gameloop(keys, stage)
        case "game_over":
            stage = gameover_gameloop.gameloop(keys, stage)
        case "planet_1":
            stage = planet1_gameloop.gameloop(keys, stage)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
