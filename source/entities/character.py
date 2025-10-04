import pygame

class Character:
    def __init__(self, name="Hero", x=100, y=100):
        self.name = name
        self.size = 50
        self.x = x
        self.y = y
        self.orientation = "up"
        self.moving = False
        self.graphic_state = 1
        self.speed = 5

        # --- Grafiken laden ---
        self.graphics_front_1_original = pygame.image.load("assets/character/character_front_1.png").convert_alpha()
        self.graphics_front_2_original = pygame.image.load("assets/character/character_front_2.png").convert_alpha()
        self.graphics_back_1_original  = pygame.image.load("assets/character/character_back_1.png").convert_alpha()
        self.graphics_back_2_original  = pygame.image.load("assets/character/character_back_2.png").convert_alpha()
        self.graphics_left_1_original  = pygame.image.load("assets/character/character_left_1.png").convert_alpha()
        self.graphics_left_2_original  = pygame.image.load("assets/character/character_left_2.png").convert_alpha()
        self.graphics_right_1_original = pygame.image.load("assets/character/character_right_1.png").convert_alpha()
        self.graphics_right_2_original = pygame.image.load("assets/character/character_right_2.png").convert_alpha()

        # Einheitlich skalieren
        target_size = (self.size, int(self.size * 1.4))
        self.graphics_front_1 = pygame.transform.scale(self.graphics_front_1_original, target_size)
        self.graphics_front_2 = pygame.transform.scale(self.graphics_front_2_original, target_size)
        self.graphics_back_1  = pygame.transform.scale(self.graphics_back_1_original,  target_size)
        self.graphics_back_2  = pygame.transform.scale(self.graphics_back_2_original,  target_size)
        self.graphics_left_1  = pygame.transform.scale(self.graphics_left_1_original,  target_size)
        self.graphics_left_2  = pygame.transform.scale(self.graphics_left_2_original,  target_size)
        self.graphics_right_1 = pygame.transform.scale(self.graphics_right_1_original, target_size)
        self.graphics_right_2 = pygame.transform.scale(self.graphics_right_2_original, target_size)

        # --- Masken für alle Frames vorab bauen (schnell zur Laufzeit) ---
        self.masks = {
            ("up",   1): pygame.mask.from_surface(self.graphics_back_1),
            ("up",   2): pygame.mask.from_surface(self.graphics_back_2),
            ("down", 1): pygame.mask.from_surface(self.graphics_front_1),
            ("down", 2): pygame.mask.from_surface(self.graphics_front_2),
            ("left", 1): pygame.mask.from_surface(self.graphics_left_1),
            ("left", 2): pygame.mask.from_surface(self.graphics_left_2),
            ("right",1): pygame.mask.from_surface(self.graphics_right_1),
            ("right",2): pygame.mask.from_surface(self.graphics_right_2),
        }

        # Start-rect (Größe entspricht jeder Surface)
        self.rect = self.current_surface().get_rect(topleft=(self.x, self.y))

    # Aktuelle Surface je nach Blickrichtung + Schrittzustand
    def current_surface(self):
        if self.orientation == "up":
            return self.graphics_back_1 if self.graphic_state == 1 else self.graphics_back_2
        if self.orientation == "down":
            return self.graphics_front_1 if self.graphic_state == 1 else self.graphics_front_2
        if self.orientation == "left":
            return self.graphics_left_1 if self.graphic_state == 1 else self.graphics_left_2
        if self.orientation == "right":
            return self.graphics_right_1 if self.graphic_state == 1 else self.graphics_right_2
        return self.graphics_front_1

    def current_mask(self):
        return self.masks[(self.orientation, self.graphic_state)]

    def draw(self, surface):
        # Animation toggeln wenn in Bewegung
        if self.moving:
            self.graphic_state = 1 if (pygame.time.get_ticks() % 600 < 300) else 2
        img = self.current_surface()
        # rect an Position anpassen (falls Größe/Frame wechselt)
        self.rect = img.get_rect(topleft=(self.x, self.y))
        surface.blit(img, (self.x, self.y))

    def _would_collide(self, new_x, new_y, objects):
        """Masken-Kollision des aktuellen Frames an neuer Position prüfen."""
        img = self.current_surface()
        mask_char = self.current_mask()
        # Virtuelle Rect an Zielposition
        test_rect = img.get_rect(topleft=(new_x, new_y))

        for obj in objects:
            # Wir erwarten, dass obj.rect und obj.mask existieren (z. B. ShipGround)
            if not hasattr(obj, "rect") or not hasattr(obj, "mask"):
                # Fallback: einfache Rechteckkollision, falls Objekt keine Maske hat
                if test_rect.colliderect(pygame.Rect(obj.x, obj.y, obj.graphic.get_width(), obj.graphic.get_height())):
                    return True
                continue

            # Grobtest: Rects überlappen?
            if not test_rect.colliderect(obj.rect):
                continue

            # Feintest: Masken-Overlap
            # Offset = Differenz der linken oberen Ecken (Char-Perspektive)
            offset = (obj.rect.left - test_rect.left, obj.rect.top - test_rect.top)
            if mask_char.overlap(obj.mask, offset):
                return True
        return False

    def react_to_keypress(self, keys, width, height, objects):
        self.moving = False
        x_neu, y_neu = self.x, self.y

        if keys[pygame.K_w]:
            self.orientation = "up";    self.moving = True; y_neu -= self.speed
        if keys[pygame.K_s]:
            self.orientation = "down";  self.moving = True; y_neu += self.speed
        if keys[pygame.K_a]:
            self.orientation = "left";  self.moving = True; x_neu -= self.speed
        if keys[pygame.K_d]:
            self.orientation = "right"; self.moving = True; x_neu += self.speed

        if not self.moving:
            return

        # Bildschirmgrenzen beachten (mit aktueller Framegröße)
        img = self.current_surface()
        w, h = img.get_size()
        if x_neu < 0: x_neu = 0
        if y_neu < 0: y_neu = 0
        if x_neu > width  - w: x_neu = width  - w
        if y_neu > height - h: y_neu = height - h

        # Masken-Kollision gegen Objekte prüfen
        if self._would_collide(x_neu, y_neu, objects):
            self.moving = False
            return
        
        

        # Bewegung anwenden
        self.x, self.y = x_neu, y_neu
