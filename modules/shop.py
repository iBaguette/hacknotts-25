import pygame, os, math

from modules.utilities import *
from modules.arrow import *

class Shop:

    def __init__(self):

        self.shop_icon = sprite_sheet_slice(os.path.join("assets", "spritesheets", "UI", "Icons", "Regular_07.png"), 1, 1, (2, 2))[0]
        self.button_background = sprite_sheet_slice(os.path.join("assets", "spritesheets", "UI", "Buttons", "Button_Blue.png"), 1, 1, (2, 2))[0]
        self.button_pressed = sprite_sheet_slice(os.path.join("assets", "spritesheets", "UI", "Buttons", "Button_Blue_Pressed.png"), 1, 1, (2, 2))[0]

        self.shop_position = (0, 150) # top left of image
        self.button_spacing = self.button_background.get_rect().height + 5 # added to y

        self.castle_button_red = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Buildings", "Red Buildings", "Tower.png"), 1, 1, (0.4, 0.4))[0]
        self.castle_button_blue = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Buildings", "Blue Buildings", "Tower.png"), 1, 1, (0.4, 0.4))[0]
        self.castle_button_black = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Buildings", "Black Buildings", "Tower.png"), 1, 1, (0.4, 0.4))[0]
        self.castle_button_yellow = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Buildings", "Yellow Buildings", "Tower.png"), 1, 1, (0.4, 0.4))[0]
        self.castle_buttons = [self.castle_button_red, self.castle_button_blue, self.castle_button_black, self.castle_button_yellow]
        self.castle_button_rect = pygame.Rect(self.shop_position[0], self.shop_position[1] + self.button_spacing * 1,
                                            self.button_background.get_rect().width, self.button_background.get_rect().height)
        
        self.castle_button_blit = self.castle_button_red.get_rect()
        self.castle_button_blit.center = self.castle_button_rect.center
        self.castle_button_blit.centery -= 25
        self.castle_level = 0 # max 3
        self.castle_button_type = self.button_background
        self.castle_button_timer = 0

        self.archer_button_red = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Red Units", "Archer", "Archer_Shoot.png"), 8, 1, (0.9, 0.9))[3]
        self.archer_button_blue = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Blue Units", "Archer", "Archer_Shoot.png"), 8, 1, (0.9, 0.9))[3]
        self.archer_button_black = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Black Units", "Archer", "Archer_Shoot.png"), 8, 1, (0.9, 0.9))[3]
        self.archer_button_yellow = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Yellow Units", "Archer", "Archer_Shoot.png"), 8, 1, (0.9, 0.9))[3]
        self.archer_buttons = [self.archer_button_red, self.archer_button_blue, self.archer_button_black, self.archer_button_yellow]
        self.archer_button_rect = pygame.Rect(self.shop_position[0], self.shop_position[1] + self.button_spacing * 2,
                                            self.button_background.get_rect().width, self.button_background.get_rect().height)
        
        self.archer_button_blit = self.archer_button_red.get_rect()
        self.archer_button_blit.center = self.archer_button_rect.center
        self.archer_button_blit.centery -= 25
        self.archer_level = 0 # max 3
        self.archer_button_type = self.button_background
        self.archer_button_timer = 0

        self.arrow_button = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Red Units", "Archer", "Arrow.png"), 1, 1, (1.1, 1.1))[0]
        self.arrow_button_rect = pygame.Rect(self.shop_position[0], self.shop_position[1] + self.button_spacing * 3,
                                            self.button_background.get_rect().width, self.button_background.get_rect().height)
        
        self.arrow_button_blit = self.arrow_button.get_rect()
        self.arrow_button_blit.center = self.arrow_button_rect.center
        self.arrow_button_blit.centery -= 25
        self.arrow_level = 0 # max 1, stays pressed
        self.arrow_button_type = self.button_background


    def draw(self, screen):
        screen.blit(self.shop_icon, self.shop_position)
        screen.blit(self.castle_button_type, (self.shop_position[0], self.shop_position[1] + self.button_spacing * 1))
        screen.blit(self.archer_button_type, (self.shop_position[0], self.shop_position[1] + self.button_spacing * 2))
        screen.blit(self.arrow_button_type, (self.shop_position[0], self.shop_position[1] + self.button_spacing * 3))

        screen.blit(self.castle_buttons[self.castle_level], self.castle_button_blit)
        screen.blit(self.archer_buttons[self.archer_level], self.archer_button_blit)
        screen.blit(self.arrow_button, self.arrow_button_blit)

        self.castle_button_type = self.button_background
        self.archer_button_type = self.button_background

        if (self.castle_button_timer > 0):
            self.castle_button_timer -= 1
            self.castle_button_type = self.button_pressed

        if (self.archer_button_timer > 0):
            self.archer_button_timer -= 1
            self.archer_button_type = self.button_pressed

        if (self.castle_level == 3):
            self.castle_button_type = self.button_pressed

        if (self.archer_level == 3):
            self.archer_button_type = self.button_pressed

    def event(self, event, mouse_pos, coins, remove_coins_function):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (self.castle_button_rect.collidepoint(mouse_pos[0], mouse_pos[1])):
                if (coins >= 20 and self.archer_level < 3):
                    remove_coins_function(20)
                    self.castle_level += 1
                    self.castle_button_type = self.button_pressed
                    self.castle_button_timer = 20
                    
            if (self.archer_button_rect.collidepoint(mouse_pos[0], mouse_pos[1])):
                if (coins >= 20 and self.archer_level < 3):
                    remove_coins_function(20)
                    self.archer_level += 1
                    self.archer_button_type = self.button_pressed
                    self.archer_button_timer = 20

            if (self.arrow_button_rect.collidepoint(mouse_pos[0], mouse_pos[1])):
                if (coins >= 100 and self.arrow_level < 1):
                    remove_coins_function(100)
                    self.arrow_level = 1
                    self.arrow_button_type = self.button_pressed
