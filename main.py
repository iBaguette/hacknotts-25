#!/usr/bin/env python3
"""
Medieval Fantasy Tower Defense Game
A wave-based defense game where an archer defends against enemies,
earning XP and upgrades to eventually defeat a dragon boss.
"""

import pygame
import sys
from game.game_state import GameState
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    """Main game loop"""
    pygame.init()
    
    # Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Medieval Fantasy Defense")
    
    # Create clock for FPS control
    clock = pygame.time.Clock()
    
    # Create game state
    game_state = GameState(screen)
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game_state.handle_event(event)
        
        # Update game state
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds
        game_state.update(dt)
        
        # Render
        game_state.render()
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
