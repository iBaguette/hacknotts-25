import pygame, os, time, random, requests

from modules.background import *
from modules.shop import *
from modules.tower import *
from modules.gui import *
from modules.game import *
from modules.menu_button import *
from modules.leaderboard_item import *

screen = pygame.display.get_surface()

from modules.enemy import *
from modules.coin import *

pygame.font.init()
medieval_font = pygame.font.Font(os.path.join("assets", "fonts", "Ancient Medium.ttf"), 40)

background = Background(screen)

item1_image = sprite_sheet_slice(os.path.join("assets", "spritesheets", "UI", "Icons", "Regular_04.png"), 1, 1, (2, 2))[0]
item2_image = sprite_sheet_slice(os.path.join("assets", "spritesheets", "UI", "Icons", "Regular_05.png"), 1, 1, (2, 2))[0]
item3_image = sprite_sheet_slice(os.path.join("assets", "spritesheets", "UI", "Icons", "Regular_06.png"), 1, 1, (2, 2))[0]

offset = -80
spacing = 150
item1 = LeaderboardItem((screen.get_width()/2, (0)+offset+spacing*2), medieval_font, item1_image)
item2 = LeaderboardItem((screen.get_width()/2, (0)+offset+spacing*3), medieval_font, item2_image)
item3 = LeaderboardItem((screen.get_width()/2, (0)+offset+spacing*4), medieval_font, item3_image)
back_button = MenuButton((200, screen.get_height()-80), 1, medieval_font, "back")
data = []
sorted_data = []
data.append({"name":"None", "score":"0"})
data.append({"name":"None", "score":"0"})
data.append({"name":"None", "score":"0"})

def update_leaderboard():
    global data, sorted_data
    r = requests.get("https://hn25.ibaguette.com/leaderboard")
    data = r.json()
    if len(data) < 3:
        data.append({"name":"None", "score":"0"})
        data.append({"name":"None", "score":"0"})
        data.append({"name":"None", "score":"0"})


    sorted_data = sorted(data, key=lambda x: int(x['score']), reverse=True)


def lead_mainloop(set_menu):
    
    # Draw the background
    background.draw(screen)

    title = medieval_font.render(
            "Leaderboard", 
            True, 
            (0, 0, 0),
            None)
    screen.blit(title, (((screen.get_width()/2)-title.get_width()/2, (0)+offset+spacing*1-10)))

    item1.draw(screen, f"{sorted_data[0]['name']} : {sorted_data[0]['score']}")
    item2.draw(screen, f"{sorted_data[1]['name']} : {sorted_data[1]['score']}")
    item3.draw(screen, f"{sorted_data[2]['name']} : {sorted_data[2]['score']}")

    if (back_button.draw(screen) == 0):
        set_menu(0)
        back_button.click_delay = -1


def lead_event(event):

    if event.type == pygame.MOUSEBUTTONDOWN:
        back_button.event()
