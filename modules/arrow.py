import pygame, os, math

from modules.utilities import *


class Arrow(pygame.sprite.Sprite):

    def __init__(self, group, position, goal):
        pygame.sprite.Sprite.__init__(self, group)

        # Load necessary images
        self.image = pygame.image.load(os.path.join("assets", "spritesheets", "Units", "Red Units", "Archer", "Arrow.png"))
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.center = self.position
        self.goal = goal
        self.delay = 6*8

        change_x = self.position[0] - goal[0]
        change_y = self.position[1] - goal[1]

        if (change_y == 0):
            self.angle = math.atan(1) * 57.2958 + 90
        else:
            self.angle = math.atan(change_x / change_y) * 57.2958 + 90

        if (change_y < 0):
            self.angle += 180

        self.image = pygame.transform.rotate(self.image, self.angle)
        self.speed = 8

        self.arrowImage = self.image.copy()
        self.image.fill((255, 255, 255, 0), None, pygame.BLEND_RGBA_MULT)
        
        
    def draw(self, screen):

        if (self.delay == 0):
            screen.blit(self.image, self.rect)

    def update(self):
        # print("aaaa", self.delay)

        direction = pygame.Vector2(self.goal) - self.position
        distance = direction.length()

        if (distance > 0):
            self.velocity = direction.normalize() * self.speed
        else:
            self.velocity = pygame.Vector2(0, 0)

        if (self.delay > 0):
            self.delay -= 1
        else:
            self.rect.center += self.velocity
            self.image = self.arrowImage
        
        