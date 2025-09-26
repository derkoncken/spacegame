import math

def space_gameloop(space_objects, keys, screen, font):
    
    ship = space_objects[0]
    planet = space_objects[1]

    ship.react_to_keypress(keys)
    ship.apply_physics()

    screen.fill((30, 30, 40))

    text = "Velocity = " + str(200 * round(math.sqrt(ship.x_velocity**2 + ship.y_velocity**2), 1) ) + " km/h"
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))  # (10,10) = linke obere Ecke

    ship.draw(screen)
    planet.draw(screen)