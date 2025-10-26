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
        self.healthImg = pygame.image.load(os.path.join("assets", "spritesheets", "UI", "Banners", "Carved_3Slides.png"))
        self.healthBarImg = pygame.image.load(os.path.join("assets", "images", "healthBar.png"))
        self.wave_count: int = 1

        scaled_factor = 1
        self.scaledHealthBorder = pygame.transform.scale(self.healthImg, (300, 50))
        self.scaledBar = pygame.transform.scale(self.healthBarImg, ((308) * scaled_factor, 50))

        imgWidth, imgHeight = self.scaledHealthBorder.get_size()
        self.health_x = (screen.get_width() - imgWidth) // 2
        self.health_y = (screen.get_height() - imgHeight) // 2

        # properties of coin /coin animation
        self.scaledCoin = pygame.transform.scale(self.coinsImage, (100, 100))
        
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

        pass

    def draw(self, screen, coins, max_health, health):

        # properties of Health Bar
        scaled_factor = health / max_health
        self.scaledHealthBorder = pygame.transform.scale(self.healthImg, (300, 50))
        self.scaledBar = pygame.transform.scale(self.healthBarImg, ((308) * scaled_factor, 50))

        def paragraph_split(pg, max_width, x, y, color, fnt):
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
                screen.blit(text_surface, (x + 20, y + i * font.get_linesize() + 20))


        font = pygame.font.SysFont("Calibri", 14, italic = True)
        white = (255, 255, 255)
        gold = (255, 215, 0)
        black = (0, 0, 0)
        red = (255, 0, 0)
        paragraph = (
            "The middle ages is a period running from 1066 to 1485 " 
            "and many developments and well-documented history occurred during this time. "     
        )

        paragraph2 = (
            "It started in the Battle of Hastings (1066), where King Harold II was "
            "(disputedly) shot with an arrow in the eye as documented in the Bayeux Tapestry "
            "and ended during the Battle of Bosworth and the conclusion of the Wars of the "
            "Roses. What does this have to do with a hackathon?"
        )

        paragraph_split(paragraph, 500, 0, 0, black, font)
        paragraph_split(paragraph2, 500, 0, 50, black, font)

        # FPS info
        text_surface = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 20).render(
            f"FPS: {int(self.clock.get_fps())}",
            True, 
            black)
        screen.blit(text_surface, ((10, screen.get_height() - 35)))

        # Coins collected
        text_surface = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 20).render(
            "Gold Collected: " + str(coins),
            True, 
            gold)
        screen.blit(self.buttonImg, ((screen.get_width())-280, 33))
        screen.blit(text_surface, (((screen.get_width())-260, 40))) 

        # Wave Data
        text_surface = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 20).render(
            f"Wave: {self.wave_count}`",
            True, 
            gold)
        screen.blit(self.buttonImg, ((screen.get_width())/2-280, 600 ))
        screen.blit(text_surface, (((screen.get_width())/2-260, 600 ))) 

        # updating internal time
        self.time_elapsed += self.clock.get_time() / 1000.0

        # computing sine wave
        offset = math.sin(self.time_elapsed * self.speed) * self.amplitude 

        # new coin position 
        new_Rect = self.scaledCoin.get_rect()
        new_Rect.topright = (screen.get_width() - 100, 100)
        new_Rect.centery = self.base_y + offset 

        screen.blit(self.scaledCoin, new_Rect.topright)

        # Drawing the health bar onto the window 
        #  --- the red bar should update as the health decays
        print(self.health_x)
        screen.blit(self.scaledHealthBorder, (self.health_x, self.health_y - 200))
        screen.blit(self.scaledBar, (self.health_x + 20 , self.health_y - 200))

        text_surface = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 14).render(
            str(int((health / max_health) * 100)) + "% ",
            True,
            red
        )
        screen.blit(text_surface, (self.health_x + 22, self.health_y - 185)) 

        self.clock.tick(60)

        pass
        ## This function is called constantly! Use it to draw the GUI

        
    