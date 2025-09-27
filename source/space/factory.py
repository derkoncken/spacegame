from space.entities.ship import Ship
from space.entities.planet import Planet
from space.entities.star import Star
import random

def create_objects(screen):
    width, height = screen.get_size()
    # Space objects
    # Starship
    ship = Ship(x = 10000, y = 3000)
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


    spaceobjects = [ship, planets, stars]
    return spaceobjects