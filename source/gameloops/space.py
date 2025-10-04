import math
import pygame
from textdrawer import draw_textbox

class SpaceGameloop:
    def __init__(self, objects, font, screen):
        self.ship = objects[0]
        self.planets = objects[1]
        self.stars = objects[2]
        self.character = objects[3]
        self.font = font
        self.screen = screen  # screen speichern
        self.screen_width, self.screen_height = self.screen.get_size()

        self.WORLD_HEIGHT, self.WORLD_WIDTH = 40000, 80000
        self.computer_width, self.computer_height = 500, 500
        self.map_screen_width, self.map_screen_height = 800, 500
        self.computer_text_position = (70, 170)

    def gameloop(self, keys, stage):

        

        map_height = 200
        map_factor = self.WORLD_HEIGHT / map_height
        map_width = int(self.WORLD_WIDTH / map_factor)

        self.ship.react_to_keypress(keys)
        self.ship.apply_physics(self.WORLD_WIDTH, self.WORLD_HEIGHT)

        if self.ship.status <= 0:
            stage = "game_over"
            print("Game Over")
            return stage

        ship_velocity = math.sqrt(self.ship.x_velocity**2 + self.ship.y_velocity**2) * 50

        for planet in self.planets:
            dx = self.ship.x - planet.x
            dy = self.ship.y - planet.y
            distance = math.hypot(dx, dy)
            if distance < (planet.radius):
                diff = ship_velocity - self.ship.max_atmospheric_velocity
                if diff > 0 and self.ship.status > 0:
                    self.ship.status -= 0.00001 * diff**2
            if distance < (planet.radius - 1000):
                print("Landed on planet")
                stage = "planet_1"

        # Drawing
        self.screen.fill((0, 0, 0))

        for star in self.stars:
            star.draw(self.screen)

        self.ship.draw(self.screen)

        for planet in self.planets:
            planet.draw(self.screen)

        minimap_surface = pygame.Surface((map_width, map_height))
        minimap_surface.fill((13, 13, 13))

        
        computer_original = pygame.image.load("assets/computer.png").convert_alpha()
        computer = pygame.transform.scale(computer_original, (self.computer_width, self.computer_height))
        text_lines = [
            "Velocity",
            "       " + str(round(ship_velocity, 1)) + " km/h",
            "Max. Atmospheric Velocity",
            "       " + str(round(self.ship.max_atmospheric_velocity, 1)) + " km/h",
            "Status",
            "       " + str(round(self.ship.status, 1)) + " %",
            "Fuel",
            "       " + str(round(self.ship.fuel, 1)) + " / " + str(round(self.ship.max_fuel, 1)) + " L (" + str(round(100 * self.ship.fuel / self.ship.max_fuel, 1)) + " %)",
            "Mass",
            "       " + str(round(self.ship.mass, 1)) + " kg"
        ]
        draw_textbox(computer, text_lines, self.computer_text_position, self.font)
        self.screen.blit(computer, (self.screen_width - self.computer_width + 50, -50))

        
        map_screen_original = pygame.image.load("assets/map_screen.png").convert_alpha()
        map_screen = pygame.transform.scale(map_screen_original, (self.map_screen_width, self.map_screen_height))

        # Planeten als Kreise (Minimap)
        for planet in self.planets:
            planet_x = int(planet.x / self.WORLD_WIDTH * map_width)
            planet_y = int(planet.y / self.WORLD_HEIGHT * map_height)
            color = planet.color
            radius = planet.radius // 200
            pygame.draw.circle(minimap_surface, color, (planet_x, planet_y), radius)

        # Schiff als Dreieck (Minimap)
        mini_x = int(self.ship.x / self.WORLD_WIDTH * map_width)
        mini_y = int(self.ship.y / self.WORLD_HEIGHT * map_height)
        size = 10
        angle_rad = math.radians(self.ship.angle)
        p1 = (mini_x + math.cos(angle_rad) * size, mini_y - math.sin(angle_rad) * size)
        p2 = (mini_x + math.cos(angle_rad + 2.5) * size * 0.6, mini_y - math.sin(angle_rad + 2.5) * size * 0.6)
        p3 = (mini_x + math.cos(angle_rad - 2.5) * size * 0.6, mini_y - math.sin(angle_rad - 2.5) * size * 0.6)
        pygame.draw.polygon(minimap_surface, (255, 255, 0), [p1, p2, p3])

        map_screen.blit(minimap_surface, (220, 80))
        self.screen.blit(map_screen, (-50, self.screen_height - self.map_screen_height + 50))

        return stage