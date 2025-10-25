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

        # Fnt = SysFont(name, size, bold=False, italic=False)
        font = pygame.font.SysFont("Arial", 36)
        white=(255,255,255)
        paragraph = "The middle ages is a period running from 1066 to 1485 and many developments and well-documented history occurred during this time. \r\nIt started in the Battle of Hastings (1066), where King Harold II was (disputedly) shot \r\nwith an arrow in the eye as documented in the Bayeux Tapestry and ended during the Battle of Bosworth and the conclusion of the Wars of the Roses. \r\nWhat does this have to do with a hackathon?"
        txtsurf = font.render(paragraph, True, white)
        screen.blit(txtsurf,(200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))



        
            # True, 
            # (0, 0, 0),
            # None)
        # screen.blit(text_surface, (((screen.get_width())-250, (screen.get_height()-100))))
        # screen.blit(paragraph, (0, 0))

        senteneces = [s.strip() for s in paragraph.split('.') if s.strip()]

        y_offset = 10
        for sentence in senteneces:
            text_surface = font.render(sentence + '.', True, white)
            screen.blit(text_surface, (10, y_offset))
            y_offset += text_surface.get_height() + 5


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
        

        #screen.get_width()
        #screen.get_height()
        pass
        ## This function is called constantly! Use it to draw the GUI
        
    