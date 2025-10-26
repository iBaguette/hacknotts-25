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

menu_state = 0
# 0 = Main Menu
# 1 = Leaderboard
# 2 = Playing Game
# 3 = DEAD
blood_splat = pygame.mixer.Sound(os.path.join("assets", "sounds", "blood-splatter.mp3"))
blood_splat.set_volume(0.1)

background_music = pygame.mixer.Sound(os.path.join("assets", "sounds", "fantasy-adventures-wizard-journey.ogg"))
background_music.set_volume(0.5)
background_music.play(loops=999)

background = Background(screen)
tower = Tower(screen)
gui = GUI(screen)
shop = Shop()

enemy_group = pygame.sprite.Group()
frame_count = 0
spawn_enemy_every_frame: int = 60

coin_group = pygame.sprite.Group()
coins = 0
starting_coins = 100
user_name = ""
score = 0

max_health = 1000
health = max_health

enable_piercing = False

def set_name(value):
    global user_name
    user_name = value

def set_menu(value):
    global menu_state
    menu_state = value
    if (value == 2):
        # User presses play, reset some game variables
        score = 0
        coins = starting_coins

def decrease_health(value):
    global health
    health -= value

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

        if (menu_state == 0):
            menu_event(event)

        elif (menu_state == 2):
            game_event(event)

        elif (menu_state == 3):
            menu_event(event)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkgreen")

    keys = pygame.key.get_pressed()

    if (menu_state == 0):
        menu_mainloop(keys, set_name, set_menu, "Medieval Defence")

    elif (menu_state == 2):
        game_mainloop(keys, health, max_health, decrease_health)

    if (menu_state == 3):
        menu_mainloop(keys, set_name, set_menu, f"You Died :(\nScore: {score}")

    # TODO: Other menus here, Leaderboard, DEAD

    pygame.display.flip()

    # Run main clock
    dt = clock.tick(60) / 1000
    frame_count += 1
    if (frame_count % 60 == 0 and menu_state == 2):
        score += 1

pygame.quit()
