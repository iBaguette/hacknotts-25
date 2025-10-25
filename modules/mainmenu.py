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
my_font = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 30)

background = Background(screen)
tower = Tower(screen)

def menu_mainloop(keys):
    
    background.draw(screen)

    

