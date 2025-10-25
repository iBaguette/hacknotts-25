# Example file showing a circle moving on screen
import pygame, os, time, random

from modules.background import *
from modules.shop import *
from modules.tower import *
from modules.gui import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)

# Note: this import is here because the display has to be init'd before enemy is imported,
# as enemy creates a dictionary using a function requiring opacity with a screen output
from modules.enemy import *
from modules.coin import *

clock = pygame.time.Clock()
running = True
dt = 0
pygame.font.init()
pygame.mixer.init()
my_font = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 30)

centre_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pygame.display.set_caption(title="Medieval Fantasy Tower Defense: Team 67")

logo = pygame.image.load(os.path.join("assets", "logo", "hn25logo.png"))
pygame.display.set_icon(logo)

logo = pygame.image.load(os.path.join("assets", "logo", "hn25logo.png"))
pygame.display.set_icon(logo)

blood_splat = pygame.mixer.Sound(os.path.join("assets", "sounds", "blood-splatter.mp3"))
blood_splat.play()

background = Background(screen)
tower = Tower(screen)
gui = GUI(screen)
shop = Shop()

enemy_group = pygame.sprite.Group()
frame_count = 0
spawn_enemy_every_frame: int = 60

coin_group = pygame.sprite.Group()
coins = 1000

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
            tower.start_shoot(pygame.mouse.get_pos())
            shop.event(event, pygame.mouse.get_pos(), coins, remove_coins, upgrade_tower, tower.upgrade_archer, upgrade_arrow)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkgreen")
 
    keys = pygame.key.get_pressed()

    # -- Player cannot move!
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    # Draw background
    background.draw(screen)

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
        # TODO: SOMETIMES TAKE DAMAGE TO TOWER WHILE THEY ARE HERE

    # Should there be a new enemy generated?
    # TODO: make this faster and faster every time
    # random_percent_value = randint(1, 10000)

    # print(f"{random_percent_value} less than {get_enemy_type("goblin")["spawn_frame_chance_percent"]}")
    if get_enemy_type("goblin")["spawn_frame_chance_per10k"] >= randint(1, 10000):
        generate_enemy(enemy_type="goblin") if randint(1,6) < 5 else generate_enemy(enemy_type="goblin_fast")

    if get_enemy_type("knight_generic")["spawn_frame_chance_per10k"] >= randint(1, 10000):
        generate_enemy(enemy_type="knight_generic")

    if get_enemy_type("knight_golden")["spawn_frame_chance_per10k"] >= randint(1, 10000):
        generate_enemy(enemy_type="knight_golden")

        # if spawn_enemy_every_frame == 1:
        #     pass
        # else:
        #     spawn_enemy_every_frame -= 1

    # Draw and Update Sprites Array
    
    enemy_group.update()
    enemy_group.draw(screen); 

    coin_group.update(pygame.mouse.get_pos())
    coin_group.draw(screen)

    # Text/GUI
    shop.draw(screen)
    gui.draw(screen, coins)

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

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    # print("tick")
    frame_count += 1

pygame.quit()
