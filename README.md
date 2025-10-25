# Medieval Fantasy Defense

A wave-based tower defense game built with Pygame where you play as an archer defending against increasingly difficult enemies, eventually facing a dragon boss!

## Features

- **Wave-based Combat**: Fight off waves of enemies that get progressively harder
- **Shooting Mechanics**: Click to shoot arrows at enemies
- **XP System**: Earn experience points by defeating enemies
- **Loot & Powerups**: Collect magical loot and powerups dropped by enemies
- **Building Progression**: Upgrade from Base Camp → Archer Tower → Keep → Bombard Tower → Castle
- **Dynamic Zoom**: The map zooms out as you progress through building tiers
- **Boss Fight**: Face the mighty dragon boss after earning enough XP
- **Fantasy Elements**: Special powerups like Rapid Fire, Multi Shot, Piercing Arrows, and Shield

## Requirements

- Python 3.7+
- Pygame 2.5.0+

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## How to Play

```bash
# Run the game
python main.py
```

### Controls

- **WASD / Arrow Keys**: Move the archer
- **Left Click**: Shoot an arrow towards the mouse cursor
- **ESC**: Close the game window

### Gameplay

1. Start at the Base Camp with your archer
2. Click to shoot arrows at incoming enemies
3. Defeat enemies to earn XP and collect loot
4. As you gain XP, your building automatically upgrades:
   - 100 XP: Archer Tower
   - 300 XP: Keep
   - 600 XP: Bombard Tower
   - 1000 XP: Castle
5. The map zooms out with each building upgrade
6. At 1000 XP, the Dragon Boss appears - defeat it to win!

### Loot Types

- **Yellow Orbs**: Extra XP
- **Green Orbs**: Health (future feature)
- **Orange Orbs**: Damage boost (future feature)

### Powerups (Fantasy Element)

- **Rapid Fire** (Blue): Shoot arrows faster
- **Multi Shot** (Orange): Shoot multiple arrows
- **Piercing Arrows** (Purple): Arrows pierce through enemies
- **Shield** (Cyan): Temporary invulnerability

## Game Structure

```
hacknotts-25/
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── game/
│   ├── __init__.py
│   ├── constants.py     # Game configuration
│   ├── game_state.py    # Main game logic
│   ├── player.py        # Player and arrow classes
│   ├── enemies.py       # Enemy and dragon classes
│   ├── loot.py          # Loot and powerup system
│   └── wave_manager.py  # Wave spawning logic
└── test_game.py         # Test script
```

## Development

To test the game components without running the full game:

```bash
python test_game.py
```

## Future Enhancements

- Sound effects and music
- Additional enemy types
- More powerups and abilities
- Save/load functionality
- High score system
- Multiple difficulty levels
- Recruited archers AI companions