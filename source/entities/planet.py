import pygame

class Planet:
    def __init__(self, x=0, y=0, radius=1, color=(205,55,0), ship=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.ship = ship
        # Erzeuge die Surface nur einmal!
        self.circle_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.circle_surface, color, (radius, radius), radius)
        self.circle_surface.set_alpha(128)  # 128 = 50% sichtbar

    def draw(self, screen):
        width, height = screen.get_size()
        pos = (int(self.x - self.ship.x + width // 2 - self.radius), int(self.y - self.ship.y + height // 2 - self.radius))
        screen.blit(self.circle_surface, pos)

