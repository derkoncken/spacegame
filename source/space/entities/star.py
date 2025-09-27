import pygame

class Star:
    def __init__(self, x=0, y=0, radius=1, color=(100, 150, 250), ship=None, distance=1):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.ship = ship
        self.distance = distance

    def draw(self, screen):
        width, height = screen.get_size()
        relative_x = self.distance*(self.x - self.ship.x + width // 2)
        relative_y = self.distance*(self.y - self.ship.y + height // 2)
        # Wrap-Around für x und y
        relative_x = relative_x % width
        relative_y = relative_y % height

        pygame.draw.circle(screen, self.color, (int(relative_x), int(relative_y)), self.radius)
