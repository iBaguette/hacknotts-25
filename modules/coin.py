import pygame, os, math

from modules.utilities import *
from modules.arrow import *

class Coin(pygame.sprite.Sprite):

    def __init__(self, group, position, screen, end_function):
        pygame.sprite.Sprite.__init__(self, group)

        # Load necessary images
        self.image = sprite_sheet_slice(os.path.join("assets", "images", "coin1.png"), 1, 1, (0.06, 0.06))[0]
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.moving = False
        self.speed = 0.0
        self.acceleration = 0.1
        self.goal = (screen.get_width() - 30, 40)
        self.end = end_function


    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def update(self, mouse_pos):
        
        difference_to_mouse = (mouse_pos[0] - self.rect.center[0], mouse_pos[1] - self.rect.center[1])
        distance_to_mouse = math.sqrt(difference_to_mouse[0]**2 + difference_to_mouse[1]**2)

        if (distance_to_mouse < 100):
            self.moving = True

        print(distance_to_mouse, self.moving, self.speed)

        if self.moving:
            direction = pygame.Vector2(self.goal) - self.rect.center
            distance = direction.length()

            if (distance > 40):
                self.velocity = direction.normalize() * self.speed
            else:
                self.end()
                self.kill()

            self.rect.center += self.velocity  
            self.speed += self.acceleration      
