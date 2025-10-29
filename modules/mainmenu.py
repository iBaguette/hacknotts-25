import pygame, os, time

from modules import gui
from modules.background import *
from modules.shop import *
from modules.tower import *
from modules.gui import *
from modules.game import generate_enemy, get_enemy_type
from modules.menu_button import *
from modules.menu_text_field import *
from modules.particle import BloodSystem
from random import randint, randrange, random

screen = pygame.display.get_surface()

from modules.enemy import *
from modules.coin import *
from modules.particle import BloodSystem, BloodParticle
blood_system = BloodSystem()
blood_splat = pygame.mixer.Sound(os.path.join("assets", "sounds", "blood-splatter.mp3"))

pygame.font.init()
medieval_font = pygame.font.Font(os.path.join("assets", "fonts", "Ancient Medium.ttf"), 60)

background = Background(screen)
text_field = MenuTextField((screen.get_width()/2, screen.get_height()/2 -80), 1, medieval_font)
play_button = MenuButton((screen.get_width()/2, screen.get_height()/2 + 60), 1, medieval_font, "Play")
lead_button = MenuButton((screen.get_width()/2, screen.get_height()/2 + 200), 1, medieval_font, "Leaderboard")
menu_enemy_group = pygame.sprite.Group()
enemy_limit_screen = 15
enemies_screen_count = 0

global menu_switch_pending_timer_frames, should_switch_to_game
menu_switch_pending_timer_frames = 0
should_switch_to_game = False

def draw_enemies():
    # 29/10/25 - OL - Add some spawns in the main menu for fun
    # -- Start enemy spawns effect --
    goblin_chance = min(10000, int(get_enemy_type("goblin")["spawn_frame_chance_per10k"]))

    width, height = screen.get_width(), screen.get_height()
    match randint(1, 4):
        case 1:  # top
            coord_x = randint(0, width)
            coord_y = randrange(-100, 0)
        case 2:  # left
            coord_x = randrange(-100, 0)
            coord_y = randrange(0, height)
        case 3:  # bottom
            coord_x = randrange(0, width)
            coord_y = randrange(height, height+100)
        case _:  # right
            # print("Spawning on right")
            coord_x = randrange(width, width+100)
            coord_y = randrange(0, height)
    enemy_random_target = pygame.Vector2(
        # foreword: I have no idea why this works, but it does
        randint(coord_x - width//4, coord_x + width//4),
        randint(coord_y - height//4, coord_y + height//4)
    )

    if randint(1, 10000) <= goblin_chance:
        if random() < 0.3:
            enemy = generate_enemy(
                enemy_type="goblin_fast", custom_enemy_group=menu_enemy_group
            )
            enemy.attack_centre = False
            enemy.target_position = enemy_random_target
        else:
            enemy = generate_enemy(
                enemy_type="goblin", custom_enemy_group=menu_enemy_group
            )
            enemy.attack_centre = False
            enemy.target_position = enemy_random_target

    knight_generic_chance = min(
        10000, int(get_enemy_type("knight_generic")["spawn_frame_chance_per10k"])
    )
    if randint(1, 10000) <= knight_generic_chance:
        enemy = generate_enemy(
            enemy_type="knight_generic", custom_enemy_group=menu_enemy_group
        )
        enemy.attack_centre = False
        enemy.target_position = enemy_random_target

    knight_golden_chance = min(
        10000, int(get_enemy_type("knight_golden")["spawn_frame_chance_per10k"])
    )
    if randint(1, 10000) <= knight_golden_chance:
        enemy = generate_enemy(
            enemy_type="knight_golden", custom_enemy_group=menu_enemy_group
        )
        enemy.attack_centre = False
        enemy.target_position = enemy_random_target

    # -- End enemy spawns effect --


def menu_mainloop(keys, set_name, set_menu, text):
    # Draw the background
    global menu_switch_pending_timer_frames, should_switch_to_game
    background.draw(screen)

    # Spawn some enemies for visual effect
    if (len(menu_enemy_group) < enemy_limit_screen) and not should_switch_to_game:
        draw_enemies()
        # print("Visible enemies on screen:", len(menu_enemy_group))
    else:
        # print("too many enemies on screen, skipping spawn")
        pass

    # Draw and Update Sprites Array
    menu_enemy_group.update()
    menu_enemy_group.draw(screen)

    title = medieval_font.render(
            text, 
            True, 
            (0, 0, 0),
            None)
    screen.blit(title, (((screen.get_width()/2)-title.get_width()/2, (screen.get_height()/2)-250)))

    text_field.draw(screen)
    if (play_button.draw(screen) == 0):
        set_name(text_field.value)
        for enemy in menu_enemy_group:
            blood_system.spawn(enemy.rect.center, count=(randint(4, 22)))
            enemy.kill()
            blood_splat.play()

        print("debug: play button pressed")
        play_button.click_delay = 41
        should_switch_to_game = True
        menu_switch_pending_timer_frames = 40
    if (lead_button.draw(screen) == 0):
        lead_button.click_delay = -1
        set_menu(1)

    blood_system.update(screen)

    if should_switch_to_game:
        print(f"debug: switching to game in {menu_switch_pending_timer_frames} frames")
        menu_switch_pending_timer_frames -= 1
        if menu_switch_pending_timer_frames == 0:
            should_switch_to_game = False
            print("debug: switching to game now")
            set_menu(2)

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
