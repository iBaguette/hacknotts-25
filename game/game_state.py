"""Main game state management"""

import pygame
import random
from game.player import Player
from game.wave_manager import WaveManager
from game.loot import Loot, PowerUp
from game.constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GREEN, YELLOW,
    XP_PER_ENEMY, LOOT_DROP_CHANCE, POWERUP_DROP_CHANCE,
    BUILDINGS, BUILDING_ORDER
)

class GameState:
    """Main game state controller"""
    
    def __init__(self, screen):
        self.screen = screen
        
        # Create player at center
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        # Game entities
        self.enemies = []
        self.loot_items = []
        self.powerups = []
        
        # Wave management
        self.wave_manager = WaveManager(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # Building progression
        self.current_building_index = 0
        self.current_building = BUILDING_ORDER[0]
        self.zoom = BUILDINGS[self.current_building]["zoom"]
        
        # Camera for zoom
        self.camera_x = 0
        self.camera_y = 0
        
        # Game state
        self.game_over = False
        self.victory = False
        
        # Font for UI
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
    def handle_event(self, event):
        """Handle game events"""
        if not self.game_over:
            self.player.handle_event(event, self.camera_x, self.camera_y)
    
    def update(self, dt):
        """Update game state"""
        if self.game_over:
            return
        
        # Get keyboard state
        keys = pygame.key.get_pressed()
        
        # Update player
        self.player.update(dt, keys)
        
        # Update camera to follow player with zoom
        self._update_camera()
        
        # Update building progression
        self._check_building_upgrade()
        
        # Spawn new enemies
        new_enemies = self.wave_manager.update(dt, self.player.xp)
        self.enemies.extend(new_enemies)
        
        # Update enemies
        for enemy in self.enemies[:]:
            enemy.update(dt, self.player.x, self.player.y)
            
            # Check collision with player
            if enemy.get_rect().colliderect(self.player.get_rect()):
                # Player takes damage (simplified - just game over for now)
                self.game_over = True
                return
        
        # Check arrow collisions with enemies
        for arrow in self.player.arrows[:]:
            for enemy in self.enemies[:]:
                if arrow.active and enemy.active:
                    if arrow.get_rect().colliderect(enemy.get_rect()):
                        if enemy.take_damage(arrow.damage):
                            # Enemy defeated
                            self.player.add_xp(XP_PER_ENEMY)
                            self._spawn_loot(enemy.x, enemy.y)
                            
                            # Check if dragon defeated
                            if hasattr(enemy, 'is_boss') and enemy.is_boss:
                                self.victory = True
                                self.game_over = True
                            
                            self.enemies.remove(enemy)
                        arrow.active = False
                        break
        
        # Update loot
        for loot in self.loot_items[:]:
            loot.update(dt)
            if not loot.active:
                self.loot_items.remove(loot)
            elif loot.get_rect().colliderect(self.player.get_rect()):
                # Player collects loot
                if loot.loot_type == "xp":
                    self.player.add_xp(loot.value)
                self.loot_items.remove(loot)
        
        # Update powerups
        for powerup in self.powerups[:]:
            powerup.update(dt)
            if not powerup.active:
                self.powerups.remove(powerup)
            elif powerup.get_rect().colliderect(self.player.get_rect()):
                # Player collects powerup (simplified - just remove for now)
                self.powerups.remove(powerup)
    
    def render(self):
        """Render the game"""
        # Clear screen
        self.screen.fill((34, 139, 34))  # Grass green background
        
        # Draw grid/map
        self._draw_map()
        
        # Draw building
        self._draw_building()
        
        # Draw entities
        self.player.render(self.screen, self.camera_x, self.camera_y)
        
        for enemy in self.enemies:
            enemy.render(self.screen, self.camera_x, self.camera_y)
        
        for loot in self.loot_items:
            loot.render(self.screen, self.camera_x, self.camera_y)
        
        for powerup in self.powerups:
            powerup.render(self.screen, self.camera_x, self.camera_y)
        
        # Draw UI
        self._draw_ui()
        
        # Draw game over screen
        if self.game_over:
            self._draw_game_over()
    
    def _update_camera(self):
        """Update camera position based on zoom"""
        # Center camera on player with zoom
        self.camera_x = self.player.x - (SCREEN_WIDTH // 2)
        self.camera_y = self.player.y - (SCREEN_HEIGHT // 2)
    
    def _check_building_upgrade(self):
        """Check if player can upgrade building"""
        if self.current_building_index < len(BUILDING_ORDER) - 1:
            next_building = BUILDING_ORDER[self.current_building_index + 1]
            xp_required = BUILDINGS[next_building]["xp_required"]
            
            if self.player.xp >= xp_required:
                self.current_building_index += 1
                self.current_building = next_building
                self.zoom = BUILDINGS[self.current_building]["zoom"]
    
    def _spawn_loot(self, x, y):
        """Spawn loot at enemy death location"""
        # Always drop XP
        if random.random() < LOOT_DROP_CHANCE:
            loot_type = random.choice(["xp", "xp", "health", "damage"])
            loot = Loot(x, y, loot_type)
            self.loot_items.append(loot)
        
        # Chance for powerup
        if random.random() < POWERUP_DROP_CHANCE:
            powerup = PowerUp(x, y)
            self.powerups.append(powerup)
    
    def _draw_map(self):
        """Draw the game map with grid"""
        # Draw a simple grid
        grid_size = 100
        
        # Calculate visible grid range
        start_x = int(self.camera_x // grid_size) * grid_size
        start_y = int(self.camera_y // grid_size) * grid_size
        end_x = start_x + SCREEN_WIDTH + grid_size
        end_y = start_y + SCREEN_HEIGHT + grid_size
        
        # Draw vertical lines
        for x in range(start_x, end_x, grid_size):
            screen_x = x - self.camera_x
            pygame.draw.line(self.screen, (0, 100, 0), 
                           (screen_x, 0), (screen_x, SCREEN_HEIGHT), 1)
        
        # Draw horizontal lines
        for y in range(start_y, end_y, grid_size):
            screen_y = y - self.camera_y
            pygame.draw.line(self.screen, (0, 100, 0), 
                           (0, screen_y), (SCREEN_WIDTH, screen_y), 1)
    
    def _draw_building(self):
        """Draw the current building at center"""
        # Building is at the initial player spawn
        building_x = SCREEN_WIDTH // 2 - self.camera_x
        building_y = SCREEN_HEIGHT // 2 - self.camera_y
        
        # Draw different buildings based on progression
        if self.current_building == "base":
            # Small tent
            pygame.draw.polygon(self.screen, (139, 69, 19), [
                (building_x, building_y - 30),
                (building_x - 25, building_y + 10),
                (building_x + 25, building_y + 10)
            ])
        elif self.current_building == "archer_tower":
            # Tower
            pygame.draw.rect(self.screen, (128, 128, 128), 
                           (building_x - 20, building_y - 40, 40, 60))
            pygame.draw.polygon(self.screen, (160, 160, 160), [
                (building_x, building_y - 50),
                (building_x - 25, building_y - 40),
                (building_x + 25, building_y - 40)
            ])
        elif self.current_building == "keep":
            # Larger keep
            pygame.draw.rect(self.screen, (128, 128, 128), 
                           (building_x - 40, building_y - 60, 80, 80))
            pygame.draw.rect(self.screen, (160, 160, 160), 
                           (building_x - 45, building_y - 70, 20, 20))
            pygame.draw.rect(self.screen, (160, 160, 160), 
                           (building_x + 25, building_y - 70, 20, 20))
        elif self.current_building == "bombard_tower":
            # Bombard tower with cannons
            pygame.draw.rect(self.screen, (64, 64, 64), 
                           (building_x - 50, building_y - 70, 100, 90))
            # Cannons
            pygame.draw.circle(self.screen, (32, 32, 32), 
                             (building_x - 40, building_y - 20), 10)
            pygame.draw.circle(self.screen, (32, 32, 32), 
                             (building_x + 40, building_y - 20), 10)
        elif self.current_building == "castle":
            # Full castle
            pygame.draw.rect(self.screen, (128, 128, 128), 
                           (building_x - 60, building_y - 80, 120, 100))
            # Towers
            for offset in [-50, 50]:
                pygame.draw.rect(self.screen, (160, 160, 160), 
                               (building_x + offset - 10, building_y - 100, 20, 30))
            # Gate
            pygame.draw.rect(self.screen, (101, 67, 33), 
                           (building_x - 15, building_y - 10, 30, 30))
    
    def _draw_ui(self):
        """Draw UI elements"""
        # XP bar
        xp_text = self.small_font.render(f"XP: {self.player.xp}", True, YELLOW)
        self.screen.blit(xp_text, (10, 10))
        
        # Building info
        building_name = BUILDINGS[self.current_building]["name"]
        building_text = self.small_font.render(f"Building: {building_name}", True, WHITE)
        self.screen.blit(building_text, (10, 40))
        
        # Next upgrade info
        if self.current_building_index < len(BUILDING_ORDER) - 1:
            next_building = BUILDING_ORDER[self.current_building_index + 1]
            xp_needed = BUILDINGS[next_building]["xp_required"] - self.player.xp
            if xp_needed > 0:
                upgrade_text = self.small_font.render(
                    f"Next: {BUILDINGS[next_building]['name']} ({xp_needed} XP needed)", 
                    True, WHITE
                )
                self.screen.blit(upgrade_text, (10, 70))
        
        # Wave info
        wave_info = self.wave_manager.get_wave_info()
        wave_text = self.small_font.render(
            f"Wave: {wave_info['wave']}", True, WHITE
        )
        self.screen.blit(wave_text, (SCREEN_WIDTH - 150, 10))
        
        # Dragon warning
        if wave_info['dragon_spawned']:
            dragon_text = self.font.render("DRAGON BOSS!", True, (255, 0, 0))
            text_rect = dragon_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
            self.screen.blit(dragon_text, text_rect)
        
        # Controls
        controls = self.small_font.render("WASD: Move | Click: Shoot", True, WHITE)
        self.screen.blit(controls, (10, SCREEN_HEIGHT - 30))
    
    def _draw_game_over(self):
        """Draw game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        if self.victory:
            text = self.font.render("VICTORY! Dragon Defeated!", True, GREEN)
        else:
            text = self.font.render("GAME OVER", True, (255, 0, 0))
        
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(text, text_rect)
        
        # Score
        score_text = self.font.render(f"Final XP: {self.player.xp}", True, YELLOW)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        self.screen.blit(score_text, score_rect)
        
        # Restart instruction
        restart_text = self.small_font.render("Close window to exit", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70))
        self.screen.blit(restart_text, restart_rect)
