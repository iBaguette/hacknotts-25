"""Game constants and configuration"""

# Screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 100, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Game settings
INITIAL_ZOOM = 1.0
MIN_ZOOM = 0.5
ZOOM_DECREASE_RATE = 0.1

# Building progression
BUILDINGS = {
    "base": {"name": "Base Camp", "xp_required": 0, "zoom": 1.0},
    "archer_tower": {"name": "Archer Tower", "xp_required": 100, "zoom": 0.9},
    "keep": {"name": "Keep", "xp_required": 300, "zoom": 0.7},
    "bombard_tower": {"name": "Bombard Tower", "xp_required": 600, "zoom": 0.6},
    "castle": {"name": "Castle", "xp_required": 1000, "zoom": 0.5},
}

BUILDING_ORDER = ["base", "archer_tower", "keep", "bombard_tower", "castle"]

# Player settings
PLAYER_SPEED = 200
ARROW_SPEED = 400
ARROW_DAMAGE = 20
SHOOT_COOLDOWN = 0.5  # seconds

# Enemy settings
ENEMY_BASE_SPEED = 50
ENEMY_BASE_HEALTH = 50
ENEMY_BASE_DAMAGE = 10
WAVE_SPAWN_DELAY = 2.0  # seconds between enemies in a wave
WAVE_DELAY = 5.0  # seconds between waves

# XP and loot
XP_PER_ENEMY = 10
LOOT_DROP_CHANCE = 0.2  # 20% chance
POWERUP_DROP_CHANCE = 0.1  # 10% chance

# Dragon boss
DRAGON_HEALTH = 1000
DRAGON_SPEED = 30
DRAGON_DAMAGE = 50
DRAGON_XP_REQUIREMENT = 1000  # Spawns when player has this XP
