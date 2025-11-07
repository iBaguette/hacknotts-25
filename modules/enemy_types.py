import os
from modules.utilities import sprite_sheet_slice


enemy_types = {
    "goblin": {
        "spawn_frame_chance_per10k": 65,
        "drop_chance": 0.41,
        "gold_drop": 1,
        "damage": 0.4,
        "speed": 0.8,
        "spritesheet": sprite_sheet_slice(os.path.join("assets", "spritesheets", "Factions", "Goblins", "Troops", "Torch", "Red", "Torch_Red.png"), horizontal_cells=6, vertical_cells=5)
    },
    "goblin_fast": {
        "spawn_frame_chance_per10k": 50,
        "drop_chance": 0.65,
        "gold_drop": 1,
        "damage": 1,
        "speed": 2,
        "spritesheet": sprite_sheet_slice(os.path.join("assets", "spritesheets", "Factions", "Goblins", "Troops", "Torch", "Red", "Torch_Red.png"), horizontal_cells=6, vertical_cells=5)
    },
    "knight_generic": {
        "spawn_frame_chance_per10k": 20,
        "drop_chance": 0.5,
        "gold_drop": 2,
        "damage": 3,
        "speed": 1.2,
        "spritesheet": sprite_sheet_slice(os.path.join("assets", "spritesheets", "Factions", "Knights", "Troops", "Warrior", "Blue", "Warrior_Blue.png"), horizontal_cells=6, vertical_cells=8)
    },
    "knight_golden": {
        "spawn_frame_chance_per10k": 7,
        "drop_chance": 0.2,
        "gold_drop": 20,
        "damage": 5,
        "speed": 2.3,
        "spritesheet": sprite_sheet_slice(os.path.join("assets", "spritesheets", "Factions", "Knights", "Troops", "Warrior", "Yellow", "Warrior_Yellow.png"), horizontal_cells=6, vertical_cells=8)
    },
    "dragon": {
        "spawn_frame_chance_per10k": 0,  # Boss only spawns manually
        "drop_chance": 1.0,
        "gold_drop": 100,
        "damage": 20,
        "speed": 1.5,
        "health": 100,  # Much higher health for boss
        "spritesheet": sprite_sheet_slice(os.path.join("assets", "spritesheets", "Factions", "Knights", "Troops", "Warrior", "Purple", "Warrior_Purple.png"), horizontal_cells=6, vertical_cells=8, scale=(3.0, 3.0))
    }
}


def get_enemy_type(key = "goblin"):
    """
    Get the data of any enemy in `goblin | knight`
    """
    return enemy_types[key]
