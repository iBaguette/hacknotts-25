import pygame, os, math

from modules.utilities import *


class Background:

    def __init__(self, screen):
        
        # Load necessary images
        self.tilemap_normal = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Terrain", "Tilemap_color1.png"),
                                          9, 6, (2, 2))
        self.tilemap_boss = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Terrain", "Tilemap_color5.png"),
                                          9, 6, (2, 2))
        
        self.tile = self.tilemap_normal[10]
        self.columns = int(math.ceil(screen.get_width() / self.tile.get_width()))
        self.rows = int(math.ceil(screen.get_height() / self.tile.get_height()))
        self.boss_mode = False

    def set_boss_mode(self, is_boss):
        self.boss_mode = is_boss
        if is_boss:
            self.tile = self.tilemap_boss[10]
        else:
            self.tile = self.tilemap_normal[10]

    def draw(self, screen):

        for x in range(0, self.columns):
            for y in range(0, self.rows):
                screen.blit(self.tile, (x*self.tile.get_width(), y*self.tile.get_height()))
        