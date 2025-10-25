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
        self.buttonImg = pygame.image.load(os.path.join("assets", "spritesheets", "UI", "Buttons", "Button_Red_3Slides.png"))

        self.scaledCoin = pygame.transform.scale(self.coinsImage, (100, 100))
        self.scaledButton = pygame.transform.scale(self.buttonImg, (100, 100))

        self.rect = self.scaledCoin.get_rect()
        self.rect = self.scaledCoin.get_rect()

        self.rect.center = (50, 75)

        self.amplitude = 20
        self.speed = 3
        self.base_y = self.rect.centery

        # internal timer
        self.clock = pygame.time.Clock()
        self.time_elapsed = 0

        pass

    def draw(self, screen, coins):

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


        # txtsurf = font.render(paragraph, True, black)
        # screen.blit(txtsurf, (0,0))
# z,(200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height()
        # senteneces = [s.strip() for s in paragraph.split('.') if s.strip()]

        # y_offset = 10
        # for sentence in senteneces:
        #     text_surface = font.render(sentence + '.', True, white)
        #     screen.blit(text_surface, (10, y_offset))
        #     y_offset += text_surface.get_height() + 5


        # FPS info
        text_surface = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 20).render(
            f"FPS: {int(self.clock.get_fps())}",
            True, 
            black)
        screen.blit(text_surface, ((10, screen.get_height() - 35)))

        # Coins collected
        text_surface = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 20).render(
            "Coins Collected: " + str(coins), 
            True, 
            gold)
        screen.blit(self.scaledButton, ((screen.get_width())-300, 40))
        screen.blit(text_surface, (((screen.get_width())-240, 40))) 

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

        
    