import pygame, typing

from random import randint

def generate_random_positon():
    """
    Creates a random position that is somewhere around the border of the screen
    """

    coord = (randint (0, pygame.display.get_surface().get_width()), randint(pygame.display.get_surface().get_height))
    

class Enemy(pygame.sprite.Sprite):
    """
    A new enemy player that spawns randomly
    """
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

        self.rect = pygame.draw.circle(screen, center=(0,0), radius=20, color="red")

    def draw(screen):
        pass


    def update():
        """
        movementes
        """
        pass
