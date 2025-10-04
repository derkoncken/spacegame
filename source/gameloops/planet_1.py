import math
import pygame
from textdrawer import draw_textbox

class Planet1Gameloop:
    def __init__(self, objects, font, screen):
        self.ship = objects[0]
        self.planets = objects[1]
        self.stars = objects[2]
        self.character = objects[3]
        self.planet_1_objects = objects[4]
        self.font = font
        self.screen = screen  # screen speichern
        self.screen_width, self.screen_height = self.screen.get_size()
        self.tile_size = 100
        graphic_tile_original = pygame.image.load("assets/tile.png").convert_alpha()
        self.graphic_tile = pygame.transform.scale(graphic_tile_original, (self.tile_size, self.tile_size))



    def gameloop(self, keys, stage):
        
        # Ground
        self.screen.fill((0, 0, 0))
        for x in range(0, self.screen_width, self.tile_size):
            for y in range(0, self.screen_height, self.tile_size):
                self.screen.blit(self.graphic_tile, (x, y))
        # Character movement
        self.character.react_to_keypress(keys, self.screen_width, self.screen_height, self.planet_1_objects)
        # Draw character
        self.character.draw(self.screen)
        # Draw all objects
        for obj in self.planet_1_objects:
            obj.draw(self.screen)
        


        
        


        return "planet_1"
