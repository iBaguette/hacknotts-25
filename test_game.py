#!/usr/bin/env python3
"""Test script to verify game imports and basic functionality"""

import sys
import os

# Test imports
try:
    print("Testing imports...")
    from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT
    print(f"✓ Constants imported: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    
    from game.player import Player, Arrow
    print("✓ Player classes imported")
    
    from game.enemies import Enemy, Dragon
    print("✓ Enemy classes imported")
    
    from game.loot import Loot, PowerUp
    print("✓ Loot classes imported")
    
    from game.wave_manager import WaveManager
    print("✓ Wave manager imported")
    
    from game.game_state import GameState
    print("✓ Game state imported")
    
    print("\n✓ All imports successful!")
    
    # Test basic object creation
    print("\nTesting object creation...")
    player = Player(100, 100)
    print(f"✓ Player created at ({player.x}, {player.y})")
    
    enemy = Enemy(200, 200, 1)
    print(f"✓ Enemy created with health {enemy.health}")
    
    dragon = Dragon(300, 300)
    print(f"✓ Dragon created with health {dragon.health}")
    
    loot = Loot(50, 50, "xp")
    print(f"✓ Loot created of type {loot.loot_type}")
    
    powerup = PowerUp(60, 60)
    print(f"✓ PowerUp created of type {powerup.powerup_type}")
    
    wave_manager = WaveManager(800, 600)
    print(f"✓ Wave manager created")
    
    print("\n✓ All object creation tests passed!")
    print("\nGame is ready to run with: python main.py")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
