import pygame
import math

class Ship:
    def __init__(self, x=200, y=150, x_velocity=0, y_velocity=0, angle=0, angular_velocity=0):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.angle = angle
        self.angular_velocity = angular_velocity
        self.graphics_original = pygame.image.load("assets/spaceship.png").convert_alpha()  # mit Alpha (Transparenz)
        self.graphics = pygame.transform.scale(self.graphics_original, (64, 64))

    def draw(self, surface):
        width, height = surface.get_size()
        rotated_graphics = pygame.transform.rotate(self.graphics, self.angle+90)
        new_rect = rotated_graphics.get_rect(center=self.graphics.get_rect(topleft=(width / 2, height / 2)).center)
        surface.blit(rotated_graphics, new_rect.topleft)
        

    def react_to_keypress(self, keys):
        if keys[pygame.K_UP]:
            self.x_velocity = self.x_velocity + math.cos(math.radians(self.angle)) * 0.03
            self.y_velocity = self.y_velocity - math.sin(math.radians(self.angle)) * 0.03
        if keys[pygame.K_LEFT]:
            self.angular_velocity += 0.03
        if keys[pygame.K_RIGHT]:
            self.angular_velocity -= 0.03
        if keys[pygame.K_DOWN]:
            self.angular_velocity *= 0.99
            if abs(self.angular_velocity) < 0.1:
                self.angular_velocity = 0

    def apply_physics(self, MAX_X, MAX_Y):
        self.x = self.x + self.x_velocity
        self.y = self.y + self.y_velocity
        self.angle = (self.angle + self.angular_velocity) % 360
        if self.x < 0:
            self.x = MAX_X
        if self.x > MAX_X:
            self.x = 0
        if self.y < 0:
            self.y = MAX_Y
        if self.y > MAX_Y:
            self.y = 0
            