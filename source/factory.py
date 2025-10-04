from entities.ship import Ship
from entities.planet import Planet
from entities.space_specific.star import Star
from entities.character import Character
from entities.ship_ground import ShipGround
import random

def create_objects(screen):
    width, height = screen.get_size()
    # Space objects
    # Starship
    ship = Ship(x = 10000, y = 25000)
    # Planets
    planet_0 = Planet(x=10000, y=30000, radius=5000, ship=ship, color=(205,55,0))
    planet_1 = Planet(x=40000, y=10000, radius=3000, ship=ship, color=(55,150,100))
    planets = [planet_0, planet_1]
    
    # Stars
    for i in range(15):
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(1, 3)
        distance = random.randint(1, 4)
        star = Star(x=x, y=y, radius=radius, ship=ship, color=(255, 255, 255), distance=distance)
        if i == 0:
            stars = [star]
        else:
            stars.append(star)

    # Character
    character = Character()

    ship_ground = ShipGround(x=200, y=200)
    planet_1_objects = [ship_ground]

    objects = [ship, planets, stars, character, planet_1_objects]
    return objects