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

        text_surface = pygame.font.Font(os.path.join("assets", "fonts", "impact.ttf"), 30).render(
            "Gold:", 
            True, 
            (0, 0, 0),
            None)
        screen.blit(text_surface, (((screen.get_width())-250, (screen.get_height()-100))))

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

        # coin properties
        # amplitude = 50 # height of the jump
        # speed = 3 # how fast it moves up and down
        # time = 0
        # coin_y = 5 
        # coin_x = 5

        # y_offset = math.sin(time * 2 * math.pi) * amplitude
        # current_y = coin_y + y_offset

        # for x in range(10):
        #     screen.blit(self.scaledCoin(0,10))
        #     pygame.display.update()

#     def __init__(self, screen):
        
#         # Load necessary images
#         self.red_archer_idle = sprite_sheet_slice(os.path.join("assets", "spritesheets", "Units", "Red Units", "Archer", "Archer_Idle.png"),
#                                                   6, 1, (1.3, 1.3))


#         self.archer_idle = self.red_archer_idle
#         self.archer_position = (screen.get_width() / 2 - (self.archer_idle[0].get_width() / 2),
#                          screen.get_height() / 2 - (self.archer_idle[0].get_height() / 1.2))
        
#         self.frame = 0
#         self.max_frame = 6 # How many images there are in the animation
#         self.frame_speed = 0
#         self.frame_speed_max = 9 # This regulates the speed of the animation

# ### following authored by ronan 

#         screen.blit(self.archer_idle[self.frame], self.archer_position)

#         self.frame_speed += 1
#         if self.frame_speed >= self.frame_speed_max:
#             self.frame_speed = 0

#             self.frame += 1
#             if self.frame >= self.max_frame:
#                 self.frame = 0


        pass
        ## This function is called constantly! Use it to draw the GUI
        
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
        
    