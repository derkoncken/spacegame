from ship import Ship
from planet import Planet

def create_objects():
    # Space objects
    ship = Ship()
    planet = Planet(x=300, y=400, radius=50, ship=ship)
    spaceobjects = [ship, planet]
    return spaceobjects