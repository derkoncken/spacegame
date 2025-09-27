import math
import pygame

from space.minimap import draw_on_minimap

def space_gameloop(space_objects, keys, screen, font):

    WORLD_HEIGHT = 60000
    WORLD_WIDTH = 40000
    width, height = screen.get_size()
    MAP_SIZE = 0.2
    map_width = width * MAP_SIZE
    map_height = height * MAP_SIZE

    
    ship = space_objects[0]
    planets = space_objects[1]

    ship.react_to_keypress(keys)
    ship.apply_physics(WORLD_HEIGHT, WORLD_WIDTH)

    screen.fill((30, 30, 40))
    minimap_surface = pygame.Surface((map_width, map_height))  
    minimap_surface.fill((20, 20, 40))      

    text = "Velocity = " + str(round(200 * math.sqrt(ship.x_velocity**2 + ship.y_velocity**2), 1) ) + " km/h"
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))  # (10,10) = linke obere Ecke


    draw_on_minimap(space_objects, minimap_surface, map_width, map_height, WORLD_HEIGHT, WORLD_WIDTH)

    screen.blit(minimap_surface, (width - map_width, 10))  # Minimap in die obere rechte Ecke zeichnen

    ship.draw(screen)
    for planet in planets:
        planet.draw(screen)