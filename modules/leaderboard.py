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




back_button = MenuButton((200, screen.get_height()-80), 1, medieval_font, "back")


def lead_mainloop(set_menu):
    
    # Draw the background
    background.draw(screen)

    title = medieval_font.render(
            "Leaderboard", 
            True, 
            (0, 0, 0),
            None)
    screen.blit(title, (((screen.get_width()/2)-title.get_width()/2, (screen.get_height()/2)-250)))

    if (back_button.draw(screen) == 0):
        set_menu(0)
        back_button.click_delay = -1


def lead_event(event):

    if event.type == pygame.MOUSEBUTTONDOWN:
        back_button.event()
