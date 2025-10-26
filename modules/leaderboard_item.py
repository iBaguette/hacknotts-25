import pygame, os, math

from modules.utilities import *


class LeaderboardItem:

    def __init__(self, position, font : pygame.font, image : pygame.Surface):

        self.regular = sprite_sheet_slice(os.path.join("assets", "spritesheets", "UI", "Buttons", "Button_Disable_3Slides.png"), 1, 1, (2, 2))[0]
        self.image = image

        self.numberImage = image

        self.imagerect = self.image.get_rect()
        self.rect = self.regular.get_rect()
        self.rect.center = position
        self.rect.centerx = self.rect.centerx + self.imagerect.width/2 - 5
        self.value = ""
        self.font = font

        self.imagerect.bottomright = self.rect.bottomleft
        self.imagerect.centerx -= 10

        self.text  = font.render(
            self.value, 
            True, 
            (0, 0, 0),
            None)
        
    def draw(self, screen, text):
        
        self.value = text
        
        self.text  = self.font.render(
            self.value, 
            True, 
            (0, 0, 0),
            None)
        
        screen.blit(self.regular, self.rect)
        screen.blit(self.image, self.imagerect)

        self.text  = self.font.render(
            self.value, 
            True, 
            (0, 0, 0),
            None)
        screen.blit(self.text, (self.rect.centerx-self.text.get_width()/2, self.rect.centery-self.text.get_height() + 20))


    def event(self):
        pass
