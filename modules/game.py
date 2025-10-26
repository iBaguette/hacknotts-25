import pygame, os, time, random

from modules.background import *
from modules.shop import *
from modules.tower import *
from modules.gui import *
from modules.game import *

screen = pygame.display.get_surface()

from modules.enemy import *
from modules.coin import *

blood_splat = pygame.mixer.Sound(os.path.join("assets", "sounds", "blood-splatter.mp3"))
# blood_splat.play()

pygame.font.init()
my_font = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 30)

background = Background(screen)
tower = Tower(screen)
gui = GUI(screen)
shop = Shop()

enemy_group = pygame.sprite.Group()
frame_count = 0
spawn_enemy_every_frame: int = 60

coin_group = pygame.sprite.Group()
coins = 1000

global wave_hasfinished, wave, wave_framestowait, wave_duration
wave: int = 0
wave_hasfinished: bool = True
wave_framestowait: int = 150
wave_duration: int = 600

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

def game_mainloop(keys, health, max_health, decrease_health):
    global wave_hasfinished, wave_framestowait, wave, wave_duration

    # Draw background
    background.draw(screen)
    # default multiplier when not in a wave reset moment
    wave_multiplier = 1

    # Draw tower
    tower.draw(screen)
    tower.update()
    
    # Is there a collision between arrows and enemies?
    collided_enemies = pygame.sprite.groupcollide(enemy_group, tower.arrows, 0, 0)
    collided_arrows = pygame.sprite.groupcollide(tower.arrows, enemy_group, 0, 0)

    for enemy in collided_enemies:
        if random.randint(0, 10) <= 3:
            Coin(coin_group, enemy.rect.center, screen, collect_coin)

        enemy.kill()
        blood_splat.set_volume(0.4)
        blood_splat.play()
    
    if (not enable_piercing):
        for arrow in collided_arrows:
            arrow.kill()
    else:
        for arrow in tower.arrows:
            arrow.check_range(screen)

    killing_enemies = pygame.sprite.spritecollide(tower, enemy_group, 0)
    for enemy in killing_enemies:
        enemy.stop_moving()
        decrease_health(enemy.damage)
        # TODO: SOMETIMES TAKE DAMAGE TO TOWER WHILE THEY ARE HERE

    if wave_duration == 0:
        wave_hasfinished = True
        print(f"Wave {wave} over, starting wait of {wave_framestowait} frames...")

    # Should there be a new enemy generated?
    if wave_hasfinished == True:
        wave_framestowait -= 1
        if wave_framestowait == 0:
            # reset wave 
            wave += 1
            wave_multiplier = wave*1.9354

            wave_framestowait = 500 + int(6*(wave*wave_multiplier)/9)
            wave_hasfinished = False 
            wave_duration = int(300*wave_multiplier)
            gui.wave_count = wave
        
            print(f"Wave pause over, starting wave {wave} which will last {wave_duration} frames. Next gap {wave_framestowait}.")

    else:
        if get_enemy_type("goblin")["spawn_frame_chance_per10k"] >= (random.randint(1, 10000)*wave_multiplier):
            generate_enemy(enemy_type="goblin") if random.randint(1,6) < 5 else generate_enemy(enemy_type="goblin_fast")

        if wave < 5 and randint(1,2) == 1:
            if get_enemy_type("knight_generic")["spawn_frame_chance_per10k"] >= random.randint(1, 10000)*wave_multiplier:
                generate_enemy(enemy_type="knight_generic")

            if get_enemy_type("knight_golden")["spawn_frame_chance_per10k"] >= random.randint(1, 10000)*wave_multiplier:
                generate_enemy(enemy_type="knight_golden")

    # Draw and Update Sprites Array
    
    enemy_group.update()
    enemy_group.draw(screen); 

    coin_group.update(pygame.mouse.get_pos())
    coin_group.draw(screen)

    # Text/GUI
    shop.draw(screen)
    gui.draw(screen, coins, max_health, health)

    ## VERY IMPORTANT text
    if keys[pygame.K_w]:
        text_surface = my_font.render(
            "This is a **tower defense**, there is no moving!", 
            True,
            (0, 0, 0),
            None)
        screen.blit(text_surface, (((screen.get_width()/2)-250, (screen.get_height()/2)-250)))

    elif keys[pygame.K_ESCAPE]:
        running = False

    # print("tick")
    # (removed incomplete 'if wave' statement)
    # independent physics.
    # print("tick")
    wave_duration -= 1
    

def game_event(event):
    if (event.type == pygame.MOUSEBUTTONDOWN):
        tower.start_shoot(pygame.mouse.get_pos())
        shop.event(event, pygame.mouse.get_pos(), coins, remove_coins, upgrade_tower, tower.upgrade_archer, upgrade_arrow)
