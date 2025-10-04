import math
import pygame
from textdrawer import draw_textbox

class GameOverGameloop:
    def __init__(self, objects, font, screen):
        self.ship = objects[0]
        self.planets = objects[1]
        self.stars = objects[2]
        self.character = objects[3]
        self.font = font
        self.screen = screen  # screen speichern

    def gameloop(self, keys, stage):
        game_over_surface = pygame.Surface((800, 600))
        game_over_surface.fill((0, 0, 0))
        draw_textbox(game_over_surface, ["Game Over"], (100, 100), self.font)
        self.screen.blit(game_over_surface, (0, 0))
        return "game_over"
