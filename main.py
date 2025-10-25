# Example file showing a circle moving on screen
import pygame, os

from modules.background import *
from modules.tower import *
from modules.gui import *
from modules import enemy

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.font.init()
my_font = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 30)

centre_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pygame.display.set_caption(title="Medieval Fantasy Tower Defense")

logo = pygame.image.load(os.path.join("assets", "logo", "hn25logo.png"))
pygame.display.set_icon(logo)

background = Background(screen)
tower = Tower(screen)
gui = GUI(screen)

enemy_group = pygame.sprite.Group()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkgreen")
 
    pygame.draw.circle(screen, "green", centre_pos, 40)

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


    # Draw and Update Sprites Array
    # enemy_group.draw()
    enemy_group.update()

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
    print("tick")

pygame.quit()
