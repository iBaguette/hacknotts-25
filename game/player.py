"""Player archer class"""

import pygame
import math
from game.constants import (
    PLAYER_SPEED, ARROW_SPEED, ARROW_DAMAGE, SHOOT_COOLDOWN,
    GREEN, BROWN, SCREEN_WIDTH, SCREEN_HEIGHT
)

class Arrow:
    """Projectile shot by the player"""
    
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.damage = ARROW_DAMAGE
        self.active = True
        
        # Calculate direction to target
        dx = target_x - x
        dy = target_y - y
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance > 0:
            self.vx = (dx / distance) * ARROW_SPEED
            self.vy = (dy / distance) * ARROW_SPEED
        else:
            self.vx = 0
            self.vy = 0
    
    def update(self, dt):
        """Update arrow position"""
        self.x += self.vx * dt
        self.y += self.vy * dt
        
        # Deactivate if off screen
        if (self.x < 0 or self.x > SCREEN_WIDTH * 2 or 
            self.y < 0 or self.y > SCREEN_HEIGHT * 2):
            self.active = False
    
    def render(self, screen, camera_x, camera_y):
        """Render the arrow"""
        screen_x = int(self.x - camera_x)
        screen_y = int(self.y - camera_y)
        pygame.draw.circle(screen, BROWN, (screen_x, screen_y), 3)
    
    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x - 3, self.y - 3, 6, 6)


class Player:
    """Player-controlled archer"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 30
        self.shoot_cooldown = 0
        self.xp = 0
        self.arrows = []
        self.recruited_archers = []
        
    def handle_event(self, event, camera_x, camera_y):
        """Handle player input events"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            if self.shoot_cooldown <= 0:
                # Convert screen coordinates to world coordinates
                target_x = event.pos[0] + camera_x
                target_y = event.pos[1] + camera_y
                self.shoot(target_x, target_y)
    
    def shoot(self, target_x, target_y):
        """Shoot an arrow towards target"""
        arrow = Arrow(self.x, self.y, target_x, target_y)
        self.arrows.append(arrow)
        self.shoot_cooldown = SHOOT_COOLDOWN
    
    def update(self, dt, keys):
        """Update player state"""
        # Update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
        
        # Movement
        dx = 0
        dy = 0
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += 1
        
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.707
            dy *= 0.707
        
        self.x += dx * PLAYER_SPEED * dt
        self.y += dy * PLAYER_SPEED * dt
        
        # Update arrows
        for arrow in self.arrows[:]:
            arrow.update(dt)
            if not arrow.active:
                self.arrows.remove(arrow)
    
    def add_xp(self, amount):
        """Add XP to player"""
        self.xp += amount
    
    def render(self, screen, camera_x, camera_y):
        """Render the player"""
        screen_x = int(self.x - camera_x)
        screen_y = int(self.y - camera_y)
        
        # Draw player as a triangle (archer)
        points = [
            (screen_x, screen_y - self.height // 2),
            (screen_x - self.width // 2, screen_y + self.height // 2),
            (screen_x + self.width // 2, screen_y + self.height // 2)
        ]
        pygame.draw.polygon(screen, GREEN, points)
        
        # Draw arrows
        for arrow in self.arrows:
            arrow.render(screen, camera_x, camera_y)
    
    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(
            self.x - self.width // 2,
            self.y - self.height // 2,
            self.width,
            self.height
        )
