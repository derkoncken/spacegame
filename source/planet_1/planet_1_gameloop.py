import math
from pydoc import text
import pygame

from textdrawer import draw_textbox
from space.minimap import draw_on_minimap

def planet_1_gameloop(space_objects, keys, screen, font):

    WORLD_HEIGHT = 40000
    WORLD_WIDTH = 80000

    width, height = screen.get_size()

    tile_size = 100

    ship = space_objects[0]
    tile_original = pygame.image.load("assets/tile.png").convert_alpha()  # mit Alpha (Transparenz)
    tile = pygame.transform.scale(tile_original, (tile_size, tile_size))
    screen.fill((0, 0, 0))
    for x in range(0, width, tile_size):
        for y in range(0, height, tile_size):
            screen.blit(tile, (x, y))

    return "planet_1"

    


    

