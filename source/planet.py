import pygame

class Planet:
    def __init__(self, x=0, y=0, radius=1, color=(100, 150, 250), ship=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.ship = ship

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x - self.ship.x), int(self.y - self.ship.y)), self.radius)
