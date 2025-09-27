import math
from pydoc import text
import pygame

from space.minimap import draw_on_minimap
from textdrawer import draw_textbox

def space_gameloop(space_objects, keys, screen, font, stage):

    WORLD_HEIGHT = 40000
    WORLD_WIDTH = 80000
    width, height = screen.get_size()

    map_height = 200
    map_factor = WORLD_HEIGHT / map_height
    map_width = int(WORLD_WIDTH / map_factor)

    
    ship = space_objects[0]
    planets = space_objects[1]
    stars = space_objects[2]

    ship.react_to_keypress(keys)
    ship.apply_physics(WORLD_WIDTH, WORLD_HEIGHT)

    for planet in planets:
        dx = ship.x - planet.x
        dy = ship.y - planet.y
        distance = math.hypot(dx, dy)
        if distance < (planet.radius - 200):
            stage = "planet_1"

    # Drawing Screen
    screen.fill((0, 0, 0))

    for star in stars:
        star.draw(screen)
    
    ship.draw(screen)

    for planet in planets:
        planet.draw(screen)
    
    minimap_surface = pygame.Surface((map_width, map_height))  
    minimap_surface.fill((13, 13, 13)) 

    computer_height, computer_width = 800, 800
    computer_original = pygame.image.load("assets/computer.png").convert_alpha()  # mit Alpha (Transparenz)
    computer = pygame.transform.scale(computer_original, (computer_width, computer_height))
    text_lines = [
        "Velocity",
        "   " + str(round(200 * math.sqrt(ship.x_velocity**2 + ship.y_velocity**2), 1)) + " km/h",
        "Max. Entry Velocity",
        "   " + "1000 km/h"
    ]
    draw_textbox(computer, text_lines, (270, 290), font)
    screen.blit(computer, (width - computer_width + 200, -200))

    screen_width, screen_height = 800, 800
    map_screen_original = pygame.image.load("assets/map_screen.png").convert_alpha()  # mit Alpha (Transparenz)
    map_screen = pygame.transform.scale(map_screen_original, (screen_width, screen_height))
    draw_on_minimap(space_objects, minimap_surface, map_width, map_height, WORLD_WIDTH, WORLD_HEIGHT)
    map_screen.blit(minimap_surface, (220, 280))  # Minimap in die obere linke Ecke zeichnen
    screen.blit(map_screen, (-90, height - screen_height + 240))  # Minimap in die obere rechte Ecke zeichnen

    return stage






