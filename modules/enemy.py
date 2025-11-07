import pygame, math, os

# from typing import Optional
from random import randint, randrange

from modules.utilities import sprite_sheet_slice
from modules.enemy_types import *

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

    screen = pygame.display.get_surface()
    if screen is None:
        width, height = 800, 600
    else:
        width, height = screen.get_width(), screen.get_height()

    match randint(1, 4):
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
            # print("Spawning on right")
            coord_x = randrange(width, width+100)
            coord_y = randrange(0, height)
            
    # print(coord_x, coord_y)
    return float(coord_x), float(coord_y)

class Enemy(pygame.sprite.Sprite):
    """
    A new enemy player that spawns randomly
    """
    def __init__(self, enemy_group, enemy_type = "goblin"):
        global enemy_counter
        # print(f"Debug [enemy] : Creating enemy sprite with id {enemy_counter}")
        pygame.sprite.Sprite.__init__(self, enemy_group)
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.id = enemy_counter

        # 29/10/25 - OL. Toggle for tower attack, as we also want meandering enemies on menu
        self.attack_centre = True
        self.target_position = pygame.Vector2(self.area.center)

        # Store enemy type for reference
        self.enemy_type = enemy_type

        # Health: is alive or is dead
        enemy_data = get_enemy_type(enemy_type)
        self.health = enemy_data.get("health", 1)
        self.max_health = self.health

        # Load necessary images
        self.goblin_torch_attack = enemy_data["spritesheet"]
        self.frame = 0
        self.max_frame = len(self.goblin_torch_attack) - 1
        self.frame_speed = 0
        self.frame_speed_max = 9
        self.damage = enemy_data["damage"]

        # Now draw the sprite

        # print(f"Debug [enemy] : Enemy {self.id} spawned at position")

        self.image = self.goblin_torch_attack[self.frame]
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = generate_random_positon()
        self.pos = pygame.Vector2(self.rect.center)

        # pygame.draw.circle(surface=screen, color="red", center=self.coord_position, radius=20)

        enemy_counter += 1

        self.speed: float = enemy_data["speed"]
        
        # Special movement for dragon boss
        self.is_boss = (enemy_type == "dragon")
        if self.is_boss:
            self.orbit_angle = 0.0
            self.orbit_radius = 400  # Distance from center to orbit
            self.orbit_speed = 0.02  # Radians per frame

    def draw(self):

        self.frame_speed += 1
        if self.frame_speed == self.frame_speed_max:
            self.frame = (self.frame + 1) % (self.max_frame + 1)
            self.frame_speed = 0

        self.image = self.goblin_torch_attack[self.frame]

    def update(self):
        """
        Move closer to the centre
        """
        # Every frame, move a certain number of x and y positions
        # print(f"Debug [enemy] : Updating sprite {self.id}")
        # pygame.draw.rect(self.screen, "red", self.rect)

        # Generate random movement if not going for centre (i.e. is on the menu)

        # TODO: Change this to not recalculate every frame, as the centre doesn't change!
        centre_pos = pygame.Vector2(self.area.center)

        if not self.attack_centre:

            # Custom logic: the centre here is a random position!
            direction = self.target_position - self.rect.center

            if direction.length() < 1:
                self.kill()
                return
            velocity = direction.normalize() * ((self.speed)/2)

            self.pos += velocity
            self.rect.center = (round(self.pos.x), round(self.pos.y))
            self.draw()
            return

        # Special behavior for dragon boss - orbit around center
        if self.is_boss:
            # Move to orbit radius first if too far or too close
            distance_to_center = (centre_pos - pygame.Vector2(self.rect.center)).length()
            
            if distance_to_center > self.orbit_radius + 50:
                # Move toward orbit radius
                direction = centre_pos - self.rect.center
                velocity = direction.normalize() * self.speed
                self.pos += velocity
            elif distance_to_center < self.orbit_radius - 50:
                # Move away from center
                direction = self.rect.center - centre_pos
                velocity = direction.normalize() * self.speed
                self.pos += velocity
            else:
                # Orbit around the center
                self.orbit_angle += self.orbit_speed
                target_x = centre_pos.x + math.cos(self.orbit_angle) * self.orbit_radius
                target_y = centre_pos.y + math.sin(self.orbit_angle) * self.orbit_radius
                target_pos = pygame.Vector2(target_x, target_y)
                
                direction = target_pos - self.rect.center
                if direction.length() > 0:
                    velocity = direction.normalize() * self.speed
                    self.pos += velocity
            
            self.rect.center = (round(self.pos.x), round(self.pos.y))
            self.draw()
            return

        # direction vector from enemy to centre
        direction = centre_pos - self.rect.center

        velocity = direction.normalize() * self.speed
        # print(direction, velocity, self.speed)

        # update float position, then update rects for rendering/collisions
        # self.rect.center += velocity
        self.pos += velocity
        self.rect.center = (round(self.pos.x), round(self.pos.y))

        self.draw()

    def stop_moving(self):
        self.speed = 0

    def take_damage(self, damage=1):
        """
        Reduce enemy health by damage amount. Returns True if enemy dies.
        """
        self.health -= damage
        return self.health <= 0
