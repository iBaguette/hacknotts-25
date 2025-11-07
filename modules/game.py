import pygame, os, time, random

from modules.background import *
from modules.shop import *
from modules.tower import *
from modules.gui import *
from modules.game import *
from modules.particle import BloodSystem, BloodParticle

screen = pygame.display.get_surface()

from modules.enemy import *
from modules.coin import *

blood_splat = pygame.mixer.Sound(os.path.join("assets", "sounds", "blood-splatter.mp3"))
new_wave = pygame.mixer.Sound(os.path.join("assets", "sounds", "netflix-intro.mp3"))
new_wave.set_volume(140)
# blood_splat.play()

pygame.font.init()
my_font = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 30)
blood_system = BloodSystem()

def reset_game_state(coin_max):
    global background, tower, gui, shop, first_wave_toggle
    global enemy_group, frame_count, spawn_enemy_every_frame
    global coin_group, coins, enable_piercing, blood_system
    global boss_spawned, boss_active, camera_zoom, target_camera_zoom

    background = Background(screen)
    tower = Tower(screen)
    gui = GUI(screen)
    shop = Shop()

    enemy_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    frame_count = 0
    spawn_enemy_every_frame = 60
    coins = coin_max
    enable_piercing = False
    first_wave_toggle = True
    
    # Reset boss fight variables
    boss_spawned = False
    boss_active = False
    camera_zoom = 1.0
    target_camera_zoom = 1.0

    blood_system.reset()

global wave_hasfinished, wave, wave_framestowait, wave_duration, wave_spawn_scale

first_wave_toggle = True
BASE_WAVE_GAP_FRAMES = 240
MIN_WAVE_GAP_FRAMES = 120
BASE_WAVE_DURATION_FRAMES = 720
MAX_WAVE_DURATION_FRAMES = 1800
WAVE_DURATION_GROWTH = 1.12
WAVE_GAP_DECAY = 0.94
WAVE_SPAWN_SCALE_GROWTH = 1.08

wave_hasfinished: bool = True
wave_framestowait: int = BASE_WAVE_GAP_FRAMES
wave_duration: int = BASE_WAVE_DURATION_FRAMES
wave_spawn_scale: float = 1.0

# Boss fight variables
boss_spawned: bool = False
boss_active: bool = False
camera_zoom: float = 1.0
target_camera_zoom: float = 1.0

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

def empty_enemy_group():
    enemy_group.empty()

def generate_enemy(enemy_type = "goblin", custom_enemy_group: Optional[pygame.sprite.Group] = None) -> Enemy:
    """
    Generate a goblin or knight
    """
    print(f"spawning {enemy_type}")

    if (custom_enemy_group is not None):
        new_enemy = Enemy(custom_enemy_group, enemy_type=enemy_type)
        return new_enemy
    else:
        new_enemy = Enemy(enemy_group, enemy_type=enemy_type)
        return new_enemy

def game_mainloop(keys, health, max_health, decrease_health, reset_health):
    global wave_hasfinished, wave_framestowait, wave_duration, wave_spawn_scale, first_wave_toggle
    global boss_spawned, boss_active, camera_zoom, target_camera_zoom

    wave: int = gui.wave_count

    # Update camera zoom smoothly
    if camera_zoom != target_camera_zoom:
        zoom_speed = 0.02
        if camera_zoom < target_camera_zoom:
            camera_zoom = min(camera_zoom + zoom_speed, target_camera_zoom)
        else:
            camera_zoom = max(camera_zoom - zoom_speed, target_camera_zoom)

    # Update background based on boss status
    background.set_boss_mode(boss_active)

    # Draw background
    background.draw(screen)
    current_spawn_scale = min(3.5, wave_spawn_scale)

    # Draw tower
    tower.draw(screen)

    tower.update()
    
    # Is there a collision between arrows and enemies?
    collided_enemies = pygame.sprite.groupcollide(enemy_group, tower.arrows, 0, 0)
    collided_arrows = pygame.sprite.groupcollide(tower.arrows, enemy_group, 0, 0)

    for enemy in collided_enemies:
        # Use new take_damage method for enemies
        is_dead = enemy.take_damage(1)
        
        if is_dead:
            # Drop coins based on enemy type configuration
            enemy_data = get_enemy_type(enemy.enemy_type)
            drop_chance = enemy_data.get("drop_chance", 0.5)
            if random.random() <= drop_chance:
                gold_amount = enemy_data.get("gold_drop", 1)
                for _ in range(gold_amount):
                    Coin(coin_group, enemy.rect.center, screen, collect_coin)

            blood_system.spawn(enemy.rect.center, count=(randint(4, 12)))
            enemy.kill()
            blood_splat.set_volume(0.4)
            blood_splat.play()
            
            # Check if boss was killed
            if hasattr(enemy, 'enemy_type') and enemy.enemy_type == "dragon":
                boss_active = False
                target_camera_zoom = 1.0  # Zoom back to normal
        else:
            # Enemy took damage but didn't die - show blood effect
            blood_system.spawn(enemy.rect.center, count=(randint(2, 5)))

    if (not enable_piercing):
        for arrow in collided_arrows:
            arrow.kill()
    else:
        for arrow in tower.arrows:
            arrow.check_range(screen)

    blood_system.update(screen)

    killing_enemies = pygame.sprite.spritecollide(tower, enemy_group, 0)
    for enemy in killing_enemies:
        enemy.stop_moving()
        decrease_health(enemy.damage)
        # TODO: SOMETIMES TAKE DAMAGE TO TOWER WHILE THEY ARE HERE

    if wave_duration == 0:
        wave_hasfinished = True
        print(f"Wave {wave} over, starting wait of {wave_framestowait} frames...")

    # Should there be a new enemy generated?
    if wave_hasfinished:
        if wave_framestowait > 0:
            wave_framestowait -= 1
        if wave_framestowait == 0 and len(enemy_group) == 0:
            if first_wave_toggle:
                first_wave_toggle = False
            else:
                gui.wave_count += 1
            wave_spawn_scale *= WAVE_SPAWN_SCALE_GROWTH
            current_spawn_scale = min(3.5, wave_spawn_scale)
            wave_framestowait = max(
                MIN_WAVE_GAP_FRAMES,
                int(BASE_WAVE_GAP_FRAMES * (WAVE_GAP_DECAY ** gui.wave_count))
            )
            wave_hasfinished = False
            wave_duration = min(
                MAX_WAVE_DURATION_FRAMES,
                int(BASE_WAVE_DURATION_FRAMES * (WAVE_DURATION_GROWTH ** (gui.wave_count - 1)))
            )
            print(f"Wave pause over, starting wave {gui.wave_count} which will last {wave_duration} frames. Next gap {wave_framestowait}.")
            new_wave.play()
            
            # Spawn dragon boss at wave 10
            if gui.wave_count == 10 and not boss_spawned:
                boss_spawned = True
                boss_active = True
                target_camera_zoom = 0.7  # Zoom out to show more of the arena
                generate_enemy(enemy_type="dragon")
                print("BOSS FIGHT: Dragon has appeared!")
    else:
        # Normal enemy spawning (skip if boss is active)
        if not boss_active:
            goblin_chance = min(10000, int(get_enemy_type("goblin")["spawn_frame_chance_per10k"] * current_spawn_scale))
            if random.randint(1, 10000) <= goblin_chance:
                fast_bias = min(0.25 + 0.05 * gui.wave_count, 0.7)
                if random.random() < fast_bias:
                    generate_enemy(enemy_type="goblin_fast")
                else:
                    generate_enemy(enemy_type="goblin")

            if wave >= 3:
                knight_generic_chance = min(10000, int(get_enemy_type("knight_generic")["spawn_frame_chance_per10k"] * current_spawn_scale * 0.85))
                if random.randint(1, 10000) <= knight_generic_chance:
                    generate_enemy(enemy_type="knight_generic")

            if wave >= 5:
                knight_golden_chance = min(10000, int(get_enemy_type("knight_golden")["spawn_frame_chance_per10k"] * current_spawn_scale * 0.65))
                if random.randint(1, 10000) <= knight_golden_chance:
                    generate_enemy(enemy_type="knight_golden")

    # Draw and Update Sprites Array
    
    enemy_group.update()
    enemy_group.draw(screen)
    
    # Draw boss health bar if boss is active
    if boss_active:
        for enemy in enemy_group:
            if hasattr(enemy, 'enemy_type') and enemy.enemy_type == "dragon":
                # Draw health bar above boss
                bar_width = 200
                bar_height = 20
                bar_x = enemy.rect.centerx - bar_width // 2
                bar_y = enemy.rect.top - 30
                
                # Background (red)
                pygame.draw.rect(screen, (100, 0, 0), (bar_x, bar_y, bar_width, bar_height))
                
                # Health (bright red)
                health_ratio = enemy.health / enemy.max_health
                pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, int(bar_width * health_ratio), bar_height))
                
                # Border
                pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height), 2)
                
                # Boss name
                boss_name_surface = my_font.render("DRAGON BOSS", True, (255, 0, 0))
                screen.blit(boss_name_surface, (bar_x + bar_width // 2 - boss_name_surface.get_width() // 2, bar_y - 25))

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
    if not wave_hasfinished:
        if wave_duration > 0:
            wave_duration -= 1
        if wave_duration <= 0 and len(enemy_group) == 0:
            wave_duration = 0
            wave_hasfinished = True
            print(f"Wave {wave} over, starting wait of {wave_framestowait} frames...")

    return empty_enemy_group

def game_event(event, upgrade_health):
    if (event.type == pygame.MOUSEBUTTONDOWN):
        tower.start_shoot(pygame.mouse.get_pos())
        shop.event(event, pygame.mouse.get_pos(), coins, remove_coins, upgrade_tower, tower.upgrade_archer, upgrade_arrow, upgrade_health)
