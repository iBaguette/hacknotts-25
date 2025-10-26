import pygame, os, time, random

from modules.background import *
from modules.shop import *
from modules.tower import *
from modules.gui import *
from modules.game import *
from modules.menu_button import *
from modules.menu_text_field import *

screen = pygame.display.get_surface()

from modules.enemy import *
from modules.coin import *

pygame.font.init()
medieval_font = pygame.font.Font(os.path.join("assets", "fonts", "Ancient Medium.ttf"), 60)

background = Background(screen)
tower = Tower(screen)
text_field = MenuTextField((screen.get_width()/2, screen.get_height()/2 -80), 1, medieval_font)
play_button = MenuButton((screen.get_width()/2, screen.get_height()/2 + 60), 1, medieval_font, "play")
lead_button = MenuButton((screen.get_width()/2, screen.get_height()/2 + 200), 1, medieval_font, "leaderboard")


def menu_mainloop(keys):
    
    # Draw the background
    background.draw(screen)

    title = medieval_font.render(
            "Medieval Defence", 
            True, 
            (0, 0, 0),
            None)
    screen.blit(title, (((screen.get_width()/2)-title.get_width()/2, (screen.get_height()/2)-250)))

    text_field.draw(screen)
    play_button.draw(screen)
    lead_button.draw(screen)


def menu_event(event):

    if event.type == pygame.KEYDOWN:
        print(event.key)







