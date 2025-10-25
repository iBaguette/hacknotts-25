"""Wave management system"""

import random
from game.enemies import Enemy, Dragon
from game.constants import WAVE_SPAWN_DELAY, WAVE_DELAY, DRAGON_XP_REQUIREMENT

class WaveManager:
    """Manages enemy waves"""
    
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.current_wave = 0
        self.enemies_in_wave = 5
        self.enemies_spawned = 0
        self.spawn_timer = 0
        self.wave_complete = False
        self.wave_delay_timer = WAVE_DELAY
        self.dragon_spawned = False
        
    def update(self, dt, player_xp):
        """Update wave spawning"""
        enemies_to_spawn = []
        
        # Check if dragon should spawn
        if player_xp >= DRAGON_XP_REQUIREMENT and not self.dragon_spawned:
            self.dragon_spawned = True
            # Spawn dragon at a random edge
            spawn_pos = self._get_spawn_position()
            dragon = Dragon(spawn_pos[0], spawn_pos[1])
            return [dragon]
        
        # Handle wave delay
        if self.wave_complete:
            self.wave_delay_timer -= dt
            if self.wave_delay_timer <= 0:
                self._start_new_wave()
            return []
        
        # Spawn enemies in current wave
        if self.enemies_spawned < self.enemies_in_wave:
            self.spawn_timer -= dt
            if self.spawn_timer <= 0:
                spawn_pos = self._get_spawn_position()
                enemy = Enemy(spawn_pos[0], spawn_pos[1], self.current_wave)
                enemies_to_spawn.append(enemy)
                self.enemies_spawned += 1
                self.spawn_timer = WAVE_SPAWN_DELAY
                
                if self.enemies_spawned >= self.enemies_in_wave:
                    self.wave_complete = True
        
        return enemies_to_spawn
    
    def _start_new_wave(self):
        """Start a new wave"""
        self.current_wave += 1
        self.enemies_in_wave = 5 + (self.current_wave * 2)  # More enemies each wave
        self.enemies_spawned = 0
        self.wave_complete = False
        self.wave_delay_timer = WAVE_DELAY
        self.spawn_timer = 0
    
    def _get_spawn_position(self):
        """Get a random spawn position at screen edges"""
        edge = random.choice(['top', 'bottom', 'left', 'right'])
        
        if edge == 'top':
            return (random.randint(0, self.screen_width * 2), -50)
        elif edge == 'bottom':
            return (random.randint(0, self.screen_width * 2), self.screen_height * 2 + 50)
        elif edge == 'left':
            return (-50, random.randint(0, self.screen_height * 2))
        else:  # right
            return (self.screen_width * 2 + 50, random.randint(0, self.screen_height * 2))
    
    def get_wave_info(self):
        """Get current wave information"""
        return {
            'wave': self.current_wave,
            'enemies_left': self.enemies_in_wave - self.enemies_spawned,
            'dragon_spawned': self.dragon_spawned
        }
