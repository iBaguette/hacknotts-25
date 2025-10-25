# Example file showing a circle moving on screen
import pygame, os

from background import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pygame.display.set_caption(title="Medieval Fantasy Tower Defense")

logo = pygame.image.load(os.path.join("assets", "logo", "hn25logo.png"))
pygame.display.set_icon(logo)

background = Background()

# Function for spritesheet handling
def sprite_sheet_slice(path, horizontal_cells, vertical_cells, scale=None):
    # load the sprite sheet
    image = pygame.image.load(path).convert_alpha()
    # get the size of the sheet

    if scale is not None:
        image = pygame.transform.scale(image, (int(scale[0] * image.get_width()), int(scale[1] * image.get_height())))

    image_size = image.get_size()

    # calculate the size of one image within the sprite sheet
    cell_width = int(image_size[0] / horizontal_cells)
    cell_height = int(image_size[1] / vertical_cells)

    # list for all the split up images
    cell_list = []

    for y in range(0, image_size[1], cell_height):
        for x in range(0, image_size[0], cell_width):
            # for all the images in the sheet, create a surface, load the section of the image to it

            # Create a temporary surface to blit parts of the image onto
            surface = pygame.Surface((cell_width, cell_height), pygame.SRCALPHA)

            surface.blit(image, (0, 0), (x, y, cell_width, cell_height))
            cell_list.append(surface)  # add the section to the list

    return cell_list  # return the list


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("darkgreen")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Draw background
    background.draw(screen)

    # Draw and Update Sprites Array



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()