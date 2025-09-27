import math
import pygame

def draw_on_minimap(space_objects, minimap_surface, map_width, map_height, world_width, world_height):
    ship = space_objects[0]
    planets = space_objects[1]
    # Planeten als Kreise
    for planet in planets:
        planet_x = int(planet.x / world_width * map_width)
        planet_y = int(planet.y / world_height * map_height)
        color = planet.color
        # Optional: Minimap-Radius proportional zum echten Radius, aber kleiner
        radius = planet.radius // 200
        pygame.draw.circle(minimap_surface, color, (planet_x, planet_y), radius)

    # Schiff als Dreieck
    mini_x = int(ship.x / world_width * map_width)
    mini_y = int(ship.y / world_height * map_height)
    size = 10
    angle_rad = math.radians(ship.angle)
    p1 = (mini_x + math.cos(angle_rad) * size, mini_y - math.sin(angle_rad) * size)
    p2 = (mini_x + math.cos(angle_rad + 2.5) * size * 0.6, mini_y - math.sin(angle_rad + 2.5) * size * 0.6)
    p3 = (mini_x + math.cos(angle_rad - 2.5) * size * 0.6, mini_y - math.sin(angle_rad - 2.5) * size * 0.6)
    pygame.draw.polygon(minimap_surface, (255, 255, 0), [p1, p2, p3])

