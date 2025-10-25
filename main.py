# Example file showing a circle moving on screen
import pygame, os, time

from modules.background import *
from modules.tower import *
from modules.coin import *
from modules.enemy import *
from modules.gui import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.font.init()
my_font = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 30)

centre_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pygame.display.set_caption(title="Medieval Fantasy Tower Defense: Team 67")

logo = pygame.image.load(os.path.join("assets", "logo", "hn25logo.png"))
pygame.display.set_icon(logo)

logo = pygame.image.load(os.path.join("assets", "logo", "hn25logo.png"))
pygame.display.set_icon(logo)

background = Background(screen)
tower = Tower(screen)
gui = GUI(screen)

enemy_group = pygame.sprite.Group()
frame_count = 0
spawn_enemy_every_frame: int = 60

coin_group = pygame.sprite.Group()
coins = 0

def collect_coin():
    global coins
    coins += 1

def generate_enemy():
    new_enemy = Enemy(enemy_group)
    return new_enemy

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            tower.start_shoot(pygame.mouse.get_pos())

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
        Coin(coin_group, enemy.rect.center, screen, collect_coin)
        enemy.kill()
    
    for arrow in collided_arrows:
        arrow.kill()

    killing_enemies = pygame.sprite.spritecollide(tower, enemy_group, 0)
    for enemy in killing_enemies:
        enemy.stop_moving()
        # TODO: SOMETIMES TAKE DAMAGE TO TOWER WHILE THEY ARE HERE

    # Should there be a new enemy generated?
    # TODO: make this faster and faster every time
    if (frame_count % spawn_enemy_every_frame) == 0:
        generate_enemy()

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
    gui.draw(screen)

    ## VERY IMPORTANT text
    if keys[pygame.K_w]:
        text_surface = my_font.render(
            "This is a **tower defense**, there is no moving!", 
            True, 
            (0, 0, 0),
            None)
        screen.blit(text_surface, (((screen.get_width()/2)-250, (screen.get_height()/2)-250)))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    # print("tick")
    frame_count += 1

pygame.quit()   