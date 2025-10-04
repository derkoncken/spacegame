import pygame


class ShipGround:
    def __init__(self, x, y, ship_size=500):
        self.x = x
        self.y = y
        self.action_x = 30
        self.action_y = 30
        self.action_radius = 10
        graphic_ship_original = pygame.image.load("assets/ship_ground.png").convert_alpha()
        self.graphic = pygame.transform.scale(
            graphic_ship_original, (ship_size, ship_size)
        )
        self.graphic = pygame.transform.rotate(self.graphic, 30)

        # rect und mask anlegen
        self.rect = self.graphic.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.graphic)

    def draw(self, screen):
        screen.blit(self.graphic, (self.x, self.y))

