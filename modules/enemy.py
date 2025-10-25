import pygame

from typing import Optional
from random import randint

enemySprite1 = pygame.sprite.Sprite()


# def generate_enemy(x_coord: Optional[int] = None, y_coord: Optional[int] = None):
#     """
#     USE THIS to create an enemny object.

#     Either creates an enemy at a given position if xcoord or ycoord is passed in. Generates randomly if either is not passed.
#     """


#     if (not(x_coord) or not(y_coord)):
#         pygame.draw.circle(screen, center=generate_random_positon(), radius=20, color="red")
    


def generate_random_positon():
    """
    Creates a random position that is somewhere around the border of the screen
    """

    coord_x, coord_y = randint(0, pygame.display.get_surface().get_width()), randint(0, pygame.display.get_surface().get_height())
             
    print(coord_x, coord_y)
    return coord_x, coord_y

class Enemy(pygame.sprite.Sprite):
    """
    A new enemy player that spawns randomly
    """
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def draw(self, screen):
        pygame.draw.circle(screen, center=generate_random_positon(), radius=20, color="red")
        

    def update():
        """
        movementes
        """
        pass


