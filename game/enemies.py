"""Enemy classes"""

import pygame
import math
import random
from game.constants import (
    ENEMY_BASE_SPEED, ENEMY_BASE_HEALTH, ENEMY_BASE_DAMAGE,
    DRAGON_HEALTH, DRAGON_SPEED, DRAGON_DAMAGE,
    RED, PURPLE, ORANGE, YELLOW
)

class Enemy:
    """Base enemy class"""
    
    def __init__(self, x, y, wave_number):
        self.x = x
        self.y = y
        self.wave_number = wave_number
        
        # Scale with wave number
        self.health = ENEMY_BASE_HEALTH + (wave_number * 10)
        self.max_health = self.health
        self.speed = ENEMY_BASE_SPEED + (wave_number * 5)
        self.damage = ENEMY_BASE_DAMAGE + (wave_number * 2)
        self.width = 15
        self.height = 15
        self.active = True
        self.color = RED
        
    def update(self, dt, player_x, player_y):
        """Move towards player"""
        dx = player_x - self.x
        dy = player_y - self.y
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance > 0:
            self.x += (dx / distance) * self.speed * dt
            self.y += (dy / distance) * self.speed * dt
    
    def take_damage(self, amount):
        """Reduce health by damage amount"""
        self.health -= amount
        if self.health <= 0:
            self.active = False
            return True
        return False
    
    def render(self, screen, camera_x, camera_y):
        """Render the enemy"""
        screen_x = int(self.x - camera_x)
        screen_y = int(self.y - camera_y)
        
        # Draw enemy as circle
        pygame.draw.circle(screen, self.color, (screen_x, screen_y), self.width)
        
        # Draw health bar
        bar_width = 30
        bar_height = 4
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, RED, 
                        (screen_x - bar_width // 2, screen_y - self.height - 10, 
                         bar_width, bar_height))
        pygame.draw.rect(screen, (0, 255, 0), 
                        (screen_x - bar_width // 2, screen_y - self.height - 10, 
                         int(bar_width * health_ratio), bar_height))
    
    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x - self.width, self.y - self.height, 
                          self.width * 2, self.height * 2)


class Dragon(Enemy):
    """Final boss - Dragon"""
    
    def __init__(self, x, y):
        super().__init__(x, y, 0)
        self.health = DRAGON_HEALTH
        self.max_health = DRAGON_HEALTH
        self.speed = DRAGON_SPEED
        self.damage = DRAGON_DAMAGE
        self.width = 40
        self.height = 40
        self.color = PURPLE
        self.is_boss = True
        
        # Special dragon abilities
        self.fire_cooldown = 0
        self.fire_rate = 2.0  # seconds between fire attacks
    
    def update(self, dt, player_x, player_y):
        """Dragon AI with special attacks"""
        super().update(dt, player_x, player_y)
        
        # Update fire cooldown
        if self.fire_cooldown > 0:
            self.fire_cooldown -= dt
    
    def render(self, screen, camera_x, camera_y):
        """Render the dragon"""
        screen_x = int(self.x - camera_x)
        screen_y = int(self.y - camera_y)
        
        # Draw dragon as a larger, distinctive shape
        # Body
        pygame.draw.circle(screen, self.color, (screen_x, screen_y), self.width)
        # Wings (triangles)
        wing_left = [
            (screen_x - self.width, screen_y),
            (screen_x - self.width - 20, screen_y - 20),
            (screen_x - self.width - 20, screen_y + 20)
        ]
        wing_right = [
            (screen_x + self.width, screen_y),
            (screen_x + self.width + 20, screen_y - 20),
            (screen_x + self.width + 20, screen_y + 20)
        ]
        pygame.draw.polygon(screen, ORANGE, wing_left)
        pygame.draw.polygon(screen, ORANGE, wing_right)
        
        # Draw health bar (larger for boss)
        bar_width = 80
        bar_height = 8
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, RED, 
                        (screen_x - bar_width // 2, screen_y - self.height - 15, 
                         bar_width, bar_height))
        pygame.draw.rect(screen, YELLOW, 
                        (screen_x - bar_width // 2, screen_y - self.height - 15, 
                         int(bar_width * health_ratio), bar_height))
