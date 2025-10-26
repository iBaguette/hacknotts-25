import pygame, os, math

from modules.utilities import *


class MenuTextField:

    def __init__(self, position, click_function, font : pygame.font, image : pygame.Surface):

        self.regular = sprite_sheet_slice(os.path.join("assets", "spritesheets", "UI", "Buttons", "Button_Disable_3Slides.png"), 1, 1, (2, 2))[0]

        self.numberImage = image

        self.rect = self.regular.get_rect()
        self.rect.center = position
        self.value = ""
        self.font = font

        self.text  = font.render(
            self.value, 
            True, 
            (0, 0, 0),
            None)
        
    def draw(self, screen):
        
        screen.blit(self.regular, self.rect)

        self.text  = self.font.render(
            self.value, 
            True, 
            (0, 0, 0),
            None)
        screen.blit(self.text, (self.rect.centerx-self.text.get_width()/2, self.rect.centery-self.text.get_height() + 20))


    def event(self):
        pass
