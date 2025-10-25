import pygame, os, math

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
        self.coinsImage = pygame.image.load(os.path.join("assets", "images", "coin1.png"))

        self.scaledCoin = pygame.transform.scale(self.coinsImage, (100, 100))

        self.rect = self.scaledCoin.get_rect()

        self.rect.center = (50, 75)

        self.amplitude = 20
        self.speed = 3
        self.base_y = self.rect.centery



        # internal timer
        self.clock = pygame.time.Clock()
        self.time_elapsed = 0

        pass

    def draw(self, screen):

        font = pygame.font.SysFont("Calibri", 14)
        white = (255, 255, 255)
        gold = (255, 215, 0)
        black = (0, 0, 0)
        paragraph = (
            "The middle ages is a period running from 1066 to 1485" 
            " and many developments and well-documented history occurred during this time. " 
            "It started in the Battle of Hastings (1066), where King Harold II was (disputedly) shot" 
            " with an arrow in the eye as documented in the Bayeux Tapestry and ended during the " 
            "Battle of Bosworth and the conclusion of the Wars of the Roses." 
            "What does this have to do with a hackathon? ")
        txtsurf = font.render(paragraph, True, black)
        screen.blit(txtsurf, (0,0))
# z,(200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height()
        # senteneces = [s.strip() for s in paragraph.split('.') if s.strip()]

        # y_offset = 10
        # for sentence in senteneces:
        #     text_surface = font.render(sentence + '.', True, white)
        #     screen.blit(text_surface, (10, y_offset))
        #     y_offset += text_surface.get_height() + 5


        # Comic Sans MS
        text_surface = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 20).render(
            f"FPS: {int(self.clock.get_fps())}",
            True, 
            black)
        screen.blit(text_surface, ((10, screen.get_height() - 35)))

        text_surface = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 20).render(
            "Gold Collected:", 
            True, 
            white)
        screen.blit(text_surface, (((screen.get_width())-250, 40)))

        # updating internal time
        self.time_elapsed += self.clock.get_time() / 1000.0

        # computing sine wave
        offset = math.sin(self.time_elapsed * self.speed) * self.amplitude 

        # new coin position 
        new_Rect = self.scaledCoin.get_rect()
        new_Rect.topright = (screen.get_width() - 100, 100)
        new_Rect.centery = self.base_y + offset 


        screen.blit(self.scaledCoin, new_Rect.topright)

        self.clock.tick(60)

        pass
        ## This function is called constantly! Use it to draw the GUI

        
    