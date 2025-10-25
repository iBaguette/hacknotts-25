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
        
    