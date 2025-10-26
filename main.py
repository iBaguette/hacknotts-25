# Example file showing a circle moving on screen
import pygame, os, time, random

from modules.background import *
from modules.shop import *
from modules.tower import *
from modules.gui import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))# , pygame.FULLSCREEN)

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

menu_state = 2
# 0 = Main Menu
# 1 = Leaderboard
# 2 = Playing Game
# 3 = DEAD
blood_splat = pygame.mixer.Sound(os.path.join("assets", "sounds", "blood-splatter.mp3"))
blood_splat.set_volume(0.1)

background_music = pygame.mixer.Sound(os.path.join("assets", "sounds", "fantasy-adventures-wizard-journey.ogg"))
background_music.set_volume(0.5)
background_music.play()

background = Background(screen)
tower = Tower(screen)
gui = GUI(screen)
shop = Shop()

enemy_group = pygame.sprite.Group()
frame_count = 0
spawn_enemy_every_frame: int = 60

coin_group = pygame.sprite.Group()
coins = 100

enable_piercing = False


def upgrade_tower():
    tower.upgrade_tower()
    # TODO: ALSO INREASE HEALTH & MAYBE HEAL RATE HERE

def upgrade_arrow():
    global enable_piercing
    enable_piercing = True

def collect_coin():
    global coins
    coins += 1

def remove_coins(value):
    global coins
    if (coins >= value):
        coins -= value


def generate_enemy(enemy_type = "goblin"):
    """
    Generate a goblin or knight
    """
    print(f"spawning {enemy_type}")
    new_enemy = Enemy(enemy_group, enemy_type=enemy_type)
    return new_enemy

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (menu_state == 2):
                game_event(event)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkgreen")
 
    keys = pygame.key.get_pressed()

    if (menu_state == 0):
        menu_mainloop(keys)

    elif (menu_state == 2):
        game_mainloop(keys)

    # TODO: Other menus here, Leaderboard, DEAD

    pygame.display.flip()

    # Run main clock
    dt = clock.tick(60) / 1000
    frame_count += 1

pygame.quit()
