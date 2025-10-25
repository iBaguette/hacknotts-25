import pygame, math

# from typing import Optional
from random import randint, randrange

global enemy_counter
enemy_counter: int = 0

# def generate_enemy(x_coord: Optional[int] = None, y_coord: Optional[int] = None):
#     """
#     USE THIS to create an enemny object.

#     Either creates an enemy at a given position if xcoord or ycoord is passed in. Generates randomly if either is not passed.
#     """

#     if (not(x_coord) or not(y_coord)):
#         pygame.draw.circle(screen, center=generate_random_positon(), radius=20, color="red")

def generate_random_positon(border_radius: int = 50):
    """
    Creates a random position that is somewhere around the border of the screen

    border_radius: int - Pixel distance from border to maximum spawn from
    """
    # Choose whether to use the top, left, bottom or right side
    side = randint(1,4)  

    screen = pygame.display.get_surface()
    if screen is None:
        width, height = 800, 600
    else:
        width, height = screen.get_width(), screen.get_height()

    match side:
        case 1:  # top
            coord_x = randint(0, width)
            coord_y = randrange(-100, 0)
        case 2:  # left
            coord_x = randrange(-100, 0)
            coord_y = randrange(0, height)
        case 3:  # bottom
            coord_x = randrange(0, width)
            coord_y = randrange(height, height+100)
        case _:  # right
            print("Spawning on right")
            coord_x = randrange(width, width+100)
            coord_y = randrange(0, height)
            
    print(coord_x, coord_y)
    return float(coord_x), float(coord_y)

class Enemy(pygame.sprite.Sprite):
    """
    A new enemy player that spawns randomly
    """
    def __init__(self, enemy_group):
        global enemy_counter
        # print(f"Debug [enemy] : Creating enemy sprite with id {enemy_counter}")
        pygame.sprite.Sprite.__init__(self, enemy_group)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.coord_position = generate_random_positon()
        self.id = enemy_counter
        radius = 20
        size = radius*2 
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (radius, radius), radius)
        self.rect = self.image.get_rect(center=self.coord_position)

        # Health: is alive or is dead
        # self.health = 1

        pygame.draw.circle(surface=screen, color="red", center=self.coord_position, radius=20)

        enemy_counter += 1
        

    def draw(self, surface):
        # print("Debug [enemy] : drawing enemy")
        surface.blit(self.image, self.rect)

    def update(self):
        """
        Move closer to the centre
        """
        # Every frame, move a certain number of x and y positions
        # print(f"Debug [enemy] : Updating sprite {self.id}")

        speed: float = 1.0

        centre_pos = pygame.Vector2(self.area.center)

        # direction vector from enemy to centre
        direction = centre_pos - self.coord_position
        distance = direction.length()

        if distance > 0:
            velocity = direction.normalize() * speed
        else:
            velocity = pygame.Vector2(0, 0)

        # update float position, then update rect for rendering/collisions
        self.coord_position += velocity
        self.rect.center = (int(self.coord_position.x), int(self.coord_position.y))
