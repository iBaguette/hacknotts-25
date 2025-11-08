import pygame, os, math

from typing import Optional
from modules.utilities import *

class GUI:
    def __init__(self, screen):
        
        # This function is called once at the start of the program
        # Use this to calcualte the positions of things
        #                       load images, etc...


        # Maybe variables for like
        # health orignally at 100 
        # hp -- hit points 
        #self.hp = 100 
        #self.coins = 0

        # Initialising 
        self.coinsImage = pygame.image.load(os.path.join("assets", "images", "coin1.png"))
        self.buttonImg = pygame.image.load(os.path.join("assets", "spritesheets", "UI", "Buttons", "Button_Red_3Slides.png"))
        self.button2Img = pygame.image.load(os.path.join("assets", "spritesheets", "UI", "Ribbons", "Ribbon_Blue_3Slides.png"))
        self.healthImg = pygame.image.load(os.path.join("assets", "spritesheets", "UI", "Banners", "Carved_3Slides.png"))
        self.healthBarImg = pygame.image.load(os.path.join("assets", "images", "healthBar.png"))
        self.wave_count: int = 1
        # Size 20 impact font for basic GUI text
        self.font_basic_impact: pygame.font.Font = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 20)
        self.font_health: pygame.font.Font = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 16)
        self.font_default: pygame.font.Font = pygame.font.Font(os.path.join("assets", "fonts", "Ancient Medium.ttf"), 22)
        self.font_paragraph = pygame.font.SysFont("Calibri", 14, italic = True)

        scaled_factor = 1
        self.scaledHealthBorder = pygame.transform.scale(self.healthImg, (300, 50))
        self.scaledBar = pygame.transform.scale(self.healthBarImg, ((308) * scaled_factor, 50))

        imgWidth, imgHeight = self.scaledHealthBorder.get_size()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.health_x = (self.screen_width - imgWidth) // 2
        self.health_y = (self.screen_height - imgHeight) // 2

        # properties of coin /coin animation
        self.scaledCoin = pygame.transform.scale(self.coinsImage, (100, 100))
        self.scaledbuttonImg = pygame.transform.scale(self.buttonImg, (228, 50))
        
        self.rect = self.scaledCoin.get_rect()

        self.rect.center = (50, 75)

        self.amplitude = 20
        self.speed = 3
        self.base_y = self.rect.centery


        # Health Bar
        # self.rect = self.borderHealth.get_rect()

        # internal timer
        self.clock = pygame.time.Clock()
        self.time_elapsed = 0

        self.white = (255, 255, 255)
        self.gold = (255, 215, 0)
        self.black = (0, 0, 0)
        self.borderColor = (0, 255, 0)


        self.paragraph = (
            "The middle ages is a period running from 1066 to 1485 " 
            "and many developments and well-documented history occurred during this time. "     
        )

        self.paragraph2 = (
            "It started in the Battle of Hastings (1066), where King Harold II was "
            "(disputedly) shot with an arrow in the eye as documented in the Bayeux Tapestry "
            "and ended during the Battle of Bosworth and the conclusion of the Wars of the "
            "Roses. What does this have to do with a hackathon?"
        )

        pass

    def paragraph_split(self, screen, pg, max_width, x, y, color, fnt):
        words = pg.split(' ')
        lines = [] 
        current_line = ""
        for word in words: 
            test_line = current_line + word + " " 
            if fnt.size(test_line)[0] < max_width:
                current_line = test_line 
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)

        for i, line in enumerate(lines):
            text_surface = fnt.render(line, True, color)
            screen.blit(text_surface, (x + 20, y + i * self.font_paragraph.get_linesize() + 20))

    def draw(self, screen, coins, max_health, health):
        """
        Draws all GUI components to the screen. Must be called every frame.
        """
        # properties of Health Bar
        scaled_factor = health / max_health
        self.scaledHealthBorder = pygame.transform.scale(self.healthImg, (300, 50))
        self.scaledBar = pygame.transform.scale(self.healthBarImg, ((215) * scaled_factor, 50)) # multiply x value by scale factor


        self.paragraph_split(screen, self.paragraph, 500, 0, 0, self.black, self.font_paragraph)
        self.paragraph_split(screen, self.paragraph2, 500, 0, 50, self.black, self.font_paragraph)

        # FPS info
        text_surface = self.font_basic_impact.render(
            f"FPS: {int(self.clock.get_fps())}",
            True, 
            self.black)
        screen.blit(text_surface, (self.screen_width - 70, self.screen_height - 35))

        # Coins collected
        text_surface = self.font_basic_impact.render(
            f"Coins Collected: {coins}",
            True, 
            self.gold)
        screen.blit(self.scaledbuttonImg, ((self.screen_width)-315, 33))
        screen.blit(text_surface, (((self.screen_width)-285, 40))) 

        # Wave Data
        text_surface = self.font_basic_impact.render(
            f"Wave: {self.wave_count}",
            True, 
            self.black)
        screen.blit(self.button2Img, (self.health_x + 57, self.health_y + 307))
        screen.blit(text_surface, (self.health_x + 120, self.health_y + 317)) 

        # updating internal time
        self.time_elapsed += self.clock.get_time() / 1000.0

        # computing sine wave
        offset = math.sin(self.time_elapsed * self.speed) * self.amplitude 

        # new coin position 
        new_Rect = self.scaledCoin.get_rect()
        new_Rect.topright = (self.screen_width - 100, 100)
        new_Rect.centery = self.base_y + offset 

        screen.blit(self.scaledCoin, new_Rect.topright)

        # Drawing the health bar onto the window 
        #  --- the red bar should update as the health decays
        screen.blit(self.scaledHealthBorder, (self.health_x, self.health_y - 200))
        screen.blit(self.scaledBar, (self.health_x + 57, self.health_y - 200))

        # print(f"[07-fix] Health: {health} / {max_health} ({(health / max_health) * 100}%)")
        health_percentage: int = round(health / max_health * 100)
        if health_percentage < 25:
            # print("[07-fix] Setting healthbar to red")
            self.borderColor = (255, 0, 0) # red
        elif health_percentage < 75:
            # print("[07-fix] Setting healthbar to amber")
            self.borderColor = (255, 191, 0) # amber
        else:
            self.borderColor = (0, 255, 0) # green

        text_surface = self.font_health.render(
            f"{health_percentage}%",
            True,
            self.borderColor
        )
        screen.blit(text_surface, (self.health_x + 22, self.health_y - 185)) 

        # Shop prices 
        # --- Tower health/upgrade
        text_surface = self.font_default.render(
            "3 Coins:",
            True,
            self.black)
        screen.blit(text_surface, (30, 260))

        # --- Bow reload speed
        text_surface = self.font_default.render(
            "3 Coins:",
            True,
            self.black)
        screen.blit(text_surface, (30, 393))

        # --- Piercing arrow
        text_surface = self.font_default.render(
            "10 Coins:",
            True,
            self.black)
        screen.blit(text_surface, (30, 526))

        # Health replenish
        text_surface = self.font_default.render(
            "7 Coins:",
            True,
            self.black)
        screen.blit(text_surface, (30, 659))


        self.clock.tick(60)

        pass
        ## This function is called constantly! Use it to draw the GUI

        
    