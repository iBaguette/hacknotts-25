"""Loot and powerup system"""

import pygame
import random
from game.constants import YELLOW, BLUE, ORANGE

class Loot:
    """Loot dropped by enemies"""
    
    def __init__(self, x, y, loot_type="xp"):
        self.x = x
        self.y = y
        self.loot_type = loot_type  # "xp", "health", "damage"
        self.active = True
        self.size = 8
        self.lifetime = 10.0  # seconds before disappearing
        
        # Set color based on type
        if loot_type == "xp":
            self.color = YELLOW
            self.value = 20
        elif loot_type == "health":
            self.color = (0, 255, 0)
            self.value = 50
        elif loot_type == "damage":
            self.color = ORANGE
            self.value = 10
    
    def update(self, dt):
        """Update loot state"""
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.active = False
    
    def render(self, screen, camera_x, camera_y):
        """Render the loot"""
        screen_x = int(self.x - camera_x)
        screen_y = int(self.y - camera_y)
        
        # Draw as a star shape
        pygame.draw.circle(screen, self.color, (screen_x, screen_y), self.size)
        
        # Pulsating effect
        pulse = int(abs(pygame.time.get_ticks() % 1000 - 500) / 100)
        pygame.draw.circle(screen, self.color, (screen_x, screen_y), 
                          self.size + pulse, 1)
    
    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x - self.size, self.y - self.size,
                          self.size * 2, self.size * 2)


class PowerUp:
    """Special powerups with magical effects"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = True
        self.size = 12
        self.lifetime = 15.0
        
        # Random powerup type
        powerup_types = [
            ("rapid_fire", BLUE, "Rapid Fire"),
            ("multi_shot", ORANGE, "Multi Shot"),
            ("piercing", (255, 0, 255), "Piercing Arrows"),
            ("shield", (0, 255, 255), "Shield")
        ]
        self.powerup_type, self.color, self.name = random.choice(powerup_types)
        self.duration = 5.0  # How long the powerup lasts when picked up
    
    def update(self, dt):
        """Update powerup state"""
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.active = False
    
    def render(self, screen, camera_x, camera_y):
        """Render the powerup"""
        screen_x = int(self.x - camera_x)
        screen_y = int(self.y - camera_y)
        
        # Draw as a glowing diamond
        points = [
            (screen_x, screen_y - self.size),
            (screen_x + self.size, screen_y),
            (screen_x, screen_y + self.size),
            (screen_x - self.size, screen_y)
        ]
        pygame.draw.polygon(screen, self.color, points)
        
        # Rotating effect
        angle = pygame.time.get_ticks() / 10
        offset = int(self.size * 0.5)
        points2 = [
            (screen_x, screen_y - offset),
            (screen_x + offset, screen_y),
            (screen_x, screen_y + offset),
            (screen_x - offset, screen_y)
        ]
        pygame.draw.polygon(screen, self.color, points2, 2)
    
    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x - self.size, self.y - self.size,
                          self.size * 2, self.size * 2)
