#!/usr/bin/env python3
"""Headless test to verify game initialization"""

import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'  # Use dummy video driver for headless

import pygame
from game.game_state import GameState
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT

print("Initializing Pygame in headless mode...")
pygame.init()

print("Creating screen...")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

print("Creating game state...")
game_state = GameState(screen)

print("Testing one frame update...")
game_state.update(0.016)  # ~60 FPS frame
game_state.render()

print("✓ Game successfully initialized and can run!")
print("✓ Player created at position:", game_state.player.x, game_state.player.y)
print("✓ Current building:", game_state.current_building)
print("✓ Wave manager active, current wave:", game_state.wave_manager.current_wave)

pygame.quit()
print("\nGame can be launched with: python main.py")
