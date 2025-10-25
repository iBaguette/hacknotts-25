import pygame

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

