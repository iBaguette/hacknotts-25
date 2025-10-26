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
text_field = MenuTextField((screen.get_width()/2, screen.get_height()/2 -80), 1, medieval_font)
play_button = MenuButton((screen.get_width()/2, screen.get_height()/2 + 60), 1, medieval_font, "Play")
lead_button = MenuButton((screen.get_width()/2, screen.get_height()/2 + 200), 1, medieval_font, "Leaderboard")


def menu_mainloop(keys, set_name, set_menu, text):
    
    # Draw the background
    background.draw(screen)

    title = medieval_font.render(
            text, 
            True, 
            (0, 0, 0),
            None)
    screen.blit(title, (((screen.get_width()/2)-title.get_width()/2, (screen.get_height()/2)-250)))

    text_field.draw(screen)
    if (play_button.draw(screen) == 0):
        set_name(text_field.value)
        play_button.click_delay = -1
        set_menu(2)
    if (lead_button.draw(screen) == 0):
        lead_button.click_delay = -1
        set_menu(1)

def menu_event(event):

    if event.type == pygame.KEYDOWN:
        if (event.key >= 97 and event.key <= 122 and len(text_field.value) < 9):
            text_field.value += pygame.key.name(event.key)
        if (event.key == 32 and len(text_field.value) < 9):
            text_field.value += " "
        if (event.key == 8):
            text_field.value = text_field.value[:-1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        play_button.event()
        lead_button.event()
