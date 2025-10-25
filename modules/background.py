import pygame, os, math

from modules.utilities import *


class Background:

    def __init__(self, screen):
        
        # Load necessary images
        self.tilemap = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Terrain", "Tilemap_color1.png"),
                                          9, 6, (2, 2))
        
        self.tile = self.tilemap[10]
        self.columns = int(math.ceil(screen.get_width() / self.tile.get_width()))
        self.rows = int(math.ceil(screen.get_height() / self.tile.get_height()))

    def draw(self, screen):

        for x in range(0, self.columns):
            for y in range(0, self.rows):
                screen.blit(self.tile, (x*self.tile.get_width(), y*self.tile.get_height()))
        