import math
from pydoc import text
import pygame

from textdrawer import draw_textbox
from space.minimap import draw_on_minimap

def game_over_gameloop(space_objects, keys, screen, font):


    # Draw Game Over Text
    game_over_surface = pygame.Surface((800, 600))
    game_over_surface.fill((0, 0, 0))
    draw_textbox(game_over_surface, ["Game Over"], (100, 100), font)
    screen.blit(game_over_surface, (0, 0))

    return "game_over"