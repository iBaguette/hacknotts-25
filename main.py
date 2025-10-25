# Example file showing a circle moving on screen
import pygame, os, time, random

from modules.background import *
from modules.shop import *
from modules.tower import *
from modules.gui import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720)) # , pygame.FULLSCREEN)

# Note: this import is here because the display has to be init'd before enemy is imported,
# as enemy creates a dictionary using a function requiring opacity with a screen output
from modules.enemy import *
from modules.coin import *
from modules.game import *
from modules.mainmenu import *

clock = pygame.time.Clock()
running = True
dt = 0

pygame.mixer.init()

centre_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pygame.display.set_caption(title="Medieval Fantasy Tower Defense: Team 67")

logo = pygame.image.load(os.path.join("assets", "logo", "hn25logo.png"))
pygame.display.set_icon(logo)

logo = pygame.image.load(os.path.join("assets", "logo", "hn25logo.png"))
pygame.display.set_icon(logo)

menu_state = 0
# 0 = Main Menu
# 1 = Leaderboard
# 2 = Playing Game
# 3 = DEAD

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            tower.start_shoot(pygame.mouse.get_pos())
            shop.event(event, pygame.mouse.get_pos(), coins, remove_coins, upgrade_tower, tower.upgrade_archer, upgrade_arrow)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkgreen")
 
    keys = pygame.key.get_pressed()

    if (menu_state == 0):
        menu_mainloop(keys)

    elif (menu_state == 2):
        game_mainloop(keys)

    # TODO: Other menus here, Leaderboard, DEAD

    # Run main clock
    dt = clock.tick(60) / 1000
    frame_count += 1

pygame.quit()
