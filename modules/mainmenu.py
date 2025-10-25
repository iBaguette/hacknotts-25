import pygame, os, time, random

from modules.background import *
from modules.shop import *
from modules.tower import *
from modules.gui import *
from modules.game import *

screen = pygame.display.get_surface()

from modules.enemy import *
from modules.coin import *

pygame.font.init()
medieval_font = pygame.font.Font(os.path.join("assets", "fonts", "Ancient Medium.ttf"), 60)

background = Background(screen)
tower = Tower(screen)

def menu_mainloop(keys):
    
    # Draw the background
    background.draw(screen)

    text_surface = medieval_font.render(
            "Medieval Defence", 
            True, 
            (0, 0, 0),
            None)
    screen.blit(text_surface, (((screen.get_width()/2)-250, (screen.get_height()/2)-250)))

