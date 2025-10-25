import pygame, os, math

from modules.utilities import *


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


        self.archer_idle = self.red_archer_idle
        self.frame = 0
        self.max_frame = 6
        self.frame_scalar = (1 * self.max_frame * self.max_frame) # Used to scale how often frames are incremented, this slows the animation down

        self.archer_position = (screen.get_width() / 2 - (self.archer_idle[0].get_width() / 2),
                         screen.get_height() / 2 - (self.archer_idle[0].get_height() / 1.2))

    def draw(self, screen):

        screen.blit(self.tower, self.tower_position)

        screen.blit(self.archer_idle[int((self.frame / self.frame_scalar)) % self.max_frame], self.archer_position)

        self.frame += 1
        if self.frame >= self.frame_scalar:
            self.frame = 0
        