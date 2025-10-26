import pygame, os, math

from modules.utilities import *
from modules.arrow import *

class Tower:

    def __init__(self, screen):
        
        # Load necessary images
        self.red_tower = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Buildings", "Red Buildings", "Tower.png"),
                                            1, 1, (2, 2))[0]
        self.blue_tower = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Buildings", "Blue Buildings", "Tower.png"),
                                            1, 1, (2, 2))[0]
        self.black_tower = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Buildings", "Black Buildings", "Tower.png"),
                                            1, 1, (2, 2))[0]
        self.yellow_tower = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Buildings", "Yellow Buildings", "Tower.png"),
                                            1, 1, (2, 2))[0]
        self.towers = [self.red_tower, self.blue_tower, self.black_tower, self.yellow_tower]
        self.tower_level = 0
        self.tower = self.red_tower        
        self.tower_position = (screen.get_width() / 2 - (self.tower.get_width() / 2),
                         screen.get_height() / 2 - (self.tower.get_height() / 2))

        self.red_archer_idle = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Red Units", "Archer", "Archer_Idle.png"),
                                                  6, 1, (1.3, 1.3))
        self.red_archer_shoot = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Red Units", "Archer", "Archer_Shoot.png"),
                                                  8, 1, (1.3, 1.3))
        
        self.blue_archer_idle = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Blue Units", "Archer", "Archer_Idle.png"),
                                                  6, 1, (1.3, 1.3))
        self.blue_archer_shoot = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Blue Units", "Archer", "Archer_Shoot.png"),
                                                  8, 1, (1.3, 1.3))
        
        self.black_archer_idle = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Black Units", "Archer", "Archer_Idle.png"),
                                                  6, 1, (1.3, 1.3))
        self.black_archer_shoot = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Black Units", "Archer", "Archer_Shoot.png"),
                                                  8, 1, (1.3, 1.3))
        
        self.yellow_archer_idle = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Yellow Units", "Archer", "Archer_Idle.png"),
                                                  6, 1, (1.3, 1.3))
        self.yellow_archer_shoot = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Yellow Units", "Archer", "Archer_Shoot.png"),
                                                  8, 1, (1.3, 1.3))
        
        self.archers = [(self.red_archer_idle, self.red_archer_shoot),
                        (self.blue_archer_idle, self.blue_archer_shoot),
                        (self.black_archer_idle, self.black_archer_shoot),
                        (self.yellow_archer_idle, self.yellow_archer_shoot)]
        
        self.archer_level = 0
        self.archer_idle = self.red_archer_idle
        self.archer_shoot = self.red_archer_shoot
        self.shoot_cooldown_set = 120
        self.shoot_cooldown = 0
        self.frame = 0
        self.max_frame = 6
        self.frame_speed = 0
        self.frame_speed_max = 9
        self.arrow_delay = 6*8
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
        self.current_wave: int = 0

    def upgrade_tower(self):
        if (self.tower_level < 3):
            self.tower_level += 1
        self.tower = self.towers[self.tower_level]

    def upgrade_archer(self):
        if (self.archer_level < 3):
            self.archer_level += 1
        self.archer_idle = self.archers[self.archer_level][0]
        self.archer_shoot = self.archers[self.archer_level][1]
        self.shoot_cooldown_set -= 35
        self.frame_speed_max -= 1
        self.arrow_delay -= 6

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
        if (self.shoot_cooldown > 0):
            self.shoot_cooldown -= 1

    def start_shoot(self, position):
        if self.shoot_cooldown == 0:
            self.shooting = True
            self.max_frame = len(self.archer_shoot) - 1
            self.frame = 0
            self.shoot_cooldown = self.shoot_cooldown_set

            Arrow(self.arrows, self.archer_rect.center, position, self.arrow_delay)
