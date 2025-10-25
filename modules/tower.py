import pygame, os, math

from modules.utilities import *
from modules.arrow import *

class Tower:

    def __init__(self, screen):
        
        # Load necessary images
        self.red_tower = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Buildings", "Red Buildings", "Tower.png"),
                                            1, 1, (2, 2))[0]

        self.tower = self.red_tower        
        self.tower_position = (screen.get_width() / 2 - (self.tower.get_width() / 2),
                         screen.get_height() / 2 - (self.tower.get_height() / 2))

        self.red_archer_idle = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Red Units", "Archer", "Archer_Idle.png"),
                                                  6, 1, (1.3, 1.3))
        self.red_archer_shoot = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Red Units", "Archer", "Archer_Shoot.png"),
                                                  8, 1, (1.3, 1.3))

        self.archer_idle = self.red_archer_idle
        self.archer_shoot = self.red_archer_shoot
        self.frame = 0
        self.max_frame = 6
        self.frame_speed = 0
        self.frame_speed_max = 9
        self.shooting = False
        self.archer_position = (screen.get_width() / 2 - (self.archer_idle[0].get_width() / 2),
                         screen.get_height() / 2 - (self.archer_idle[0].get_height() / 1.2))
        self.archer_rect = self.archer_idle[0].get_rect()
        self.archer_rect.topleft = self.archer_position
        self.arrows = pygame.sprite.Group()
        self.rect : pygame.Rect = self.tower.get_rect()
        self.rect = self.rect.inflate(-100, -300)
        self.rect.topleft = self.tower_position
        self.rect.centery += 150
        self.rect.centerx += 50

    def draw(self, screen):

        screen.blit(self.tower, self.tower_position)
        if (not self.shooting):
            screen.blit(self.archer_idle[self.frame], self.archer_position)
        else:
            screen.blit(self.archer_shoot[self.frame], self.archer_position)
        
        self.arrows.draw(screen)

        self.frame_speed += 1
        if self.frame_speed >= self.frame_speed_max:
            self.frame_speed = 0

            self.frame += 1
            if self.frame >= self.max_frame:
                self.frame = 0

                if (self.shooting):
                    self.shooting = False
                    self.max_frame = len(self.archer_idle) - 1
        #pygame.draw.rect(screen, "red", self.rect)
                    

    def update(self):
        self.arrows.update()

    def start_shoot(self, position):
        self.shooting = True
        self.max_frame = len(self.archer_shoot) - 1
        self.frame = 0

        Arrow(self.arrows, self.archer_rect.center, position)

    

        


        


        