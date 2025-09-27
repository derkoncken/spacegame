from ship import Ship
from planet import Planet

def create_objects():
    # Space objects
    ship = Ship(x = 500, y = 1000)
    planet_0 = Planet(x=10000, y=30000, radius=5000, ship=ship)
    planet_1 = Planet(x=40000, y=10000, radius=3000, ship=ship)
    planets = [planet_0, planet_1]
    spaceobjects = [ship, planets]
    return spaceobjects