import pygame, os, math

from modules.utilities import *


class MenuButton:

    def __init__(self, position, click_function, font : pygame.font, text):

        self.regular = sprite_sheet_slice(os.path.join("assets", "spritesheets", "UI", "Buttons", "Button_Blue_3Slides.png"), 1, 1, (2, 2))[0]
        self.pressed = sprite_sheet_slice(os.path.join("assets", "spritesheets", "UI", "Buttons", "Button_Blue_3Slides_Pressed.png"), 1, 1, (2, 2))[0]

        self.rect = self.regular.get_rect()
        self.rect.center = position
        self.click_delay = -1

        self.text  = font.render(
            text, 
            True, 
            (0, 0, 0),
            None)
        
    def draw(self, screen):
        if (self.click_delay > 0):
            self.click_delay -= 1
            screen.blit(self.pressed, self.rect)
        else:
            screen.blit(self.regular, self.rect)
        
        screen.blit(self.text, (self.rect.centerx-self.text.get_width()/2, self.rect.centery-self.text.get_height() + 10))
        return self.click_delay
    
    def event(self):
        if (self.rect.collidepoint(pygame.mouse.get_pos())):
            self.click_delay = 20
