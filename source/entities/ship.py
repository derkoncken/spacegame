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
        self.thrust = False
        self.right = False
        self.left = False
        self.status = 100
        self.fuel = 100
        self.max_fuel = 100
        self.mass = 1000  # in kg
        self.max_atmospheric_velocity = 100  # in units per frame
        self.graphics_spaceship_original = pygame.image.load("assets/spaceship.png").convert_alpha()  # mit Alpha (Transparenz)
        self.graphics_spaceship = pygame.transform.scale(self.graphics_spaceship_original, (200, 200))
        self.graphics_thrust_1_original = pygame.image.load("assets/thrust_1.png").convert_alpha()  # mit Alpha (Transparenz)
        self.graphics_thrust_1 = pygame.transform.scale(self.graphics_thrust_1_original, (200, 200))
        self.graphics_thrust_2_original = pygame.image.load("assets/thrust_2.png").convert_alpha()  # mit Alpha (Transparenz)
        self.graphics_thrust_2 = pygame.transform.scale(self.graphics_thrust_2_original, (200, 200))
        self.graphics_flame_1_original = pygame.image.load("assets/flame_1.png").convert_alpha()  # mit Alpha (Transparenz)
        self.graphics_flame_1 = pygame.transform.scale(self.graphics_flame_1_original, (200, 200))
        self.graphics_flame_2_original = pygame.image.load("assets/flame_2.png").convert_alpha()  # mit Alpha (Transparenz)
        self.graphics_flame_2 = pygame.transform.scale(self.graphics_flame_2_original, (200, 200))

    def draw(self, surface):
        base_graphics = self.graphics_spaceship.copy()

        if self.thrust:
            
            if pygame.time.get_ticks() % 400 < 200:
                base_graphics.blit(self.graphics_thrust_1, (0, 0))
            else:
                base_graphics.blit(self.graphics_thrust_2, (0, 0))

        if pygame.time.get_ticks() % 600 < 300:
            flame = self.graphics_flame_1
        else:
            flame = self.graphics_flame_2
        if self.right:
            rotated_flame = pygame.transform.rotate(flame, 20)
            base_graphics.blit(rotated_flame, (-30, 0))
        if self.left:
            rotated_flame = pygame.transform.rotate(flame, -20)
            base_graphics.blit(rotated_flame, (-35, 0))

        base_graphics.blit(self.graphics_spaceship, (0, 0))

        width, height = surface.get_size()
        rotated_graphics = pygame.transform.rotate(base_graphics, self.angle-90)
        new_rect = rotated_graphics.get_rect(center=(width // 2, height // 2))
        surface.blit(rotated_graphics, new_rect.topleft)
        

    def react_to_keypress(self, keys):
        self.thrust = False
        self.right = False
        self.left = False
        if keys[pygame.K_UP]:
            if self.fuel > 0:
                self.x_velocity = self.x_velocity + math.cos(math.radians(self.angle)) * 0.03
                self.y_velocity = self.y_velocity - math.sin(math.radians(self.angle)) * 0.03
                self.thrust = True
                self.fuel = max(0, self.fuel - 0.1)
        if keys[pygame.K_LEFT]:
            self.angular_velocity += 0.03
            self.left = True
        if keys[pygame.K_RIGHT]:
            self.angular_velocity -= 0.03
            self.right = True
        if keys[pygame.K_DOWN]:
            if abs(self.angular_velocity) < 0.1:
                self.angular_velocity = 0
            elif self.angular_velocity > 0:
                self.angular_velocity -= 0.03
                self.right = True
            elif self.angular_velocity < 0:
                self.angular_velocity += 0.03
                self.left = True


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
