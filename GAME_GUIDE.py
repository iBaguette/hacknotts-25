#!/usr/bin/env python3
"""
Game Demonstration and Quick Start Guide
"""

print("""
╔════════════════════════════════════════════════════════════════╗
║         MEDIEVAL FANTASY DEFENSE - GAME OVERVIEW               ║
╔════════════════════════════════════════════════════════════════╗

🎮 GAME CONCEPT:
A wave-based tower defense game where you control an archer defending
against enemies. Defeat enemies to earn XP, upgrade your base, and
eventually face the dragon boss!

📋 HOW TO PLAY:
1. Install: pip install -r requirements.txt
2. Run: python main.py
3. Move: WASD or Arrow Keys
4. Shoot: Left Click (arrows fly towards mouse cursor)

🏰 BUILDING PROGRESSION:
┌─────────────────────────────────────────────────────────────┐
│ Base Camp (Start)     →  0 XP needed                        │
│ Archer Tower          →  100 XP needed   (Zoom: 0.9x)       │
│ Keep                  →  300 XP needed   (Zoom: 0.7x)       │
│ Bombard Tower         →  600 XP needed   (Zoom: 0.6x)       │
│ Castle                →  1000 XP needed  (Zoom: 0.5x)       │
└─────────────────────────────────────────────────────────────┘

⚔️  GAME PROGRESSION:
╔═══════════════════════════════════════════════════════════════╗
║ PHASE 1: Early Game (0-100 XP)                               ║
║  • Fight weak enemies in waves                               ║
║  • Learn shooting mechanics                                  ║
║  • Collect loot drops                                        ║
║  • Upgrade to Archer Tower                                   ║
╠═══════════════════════════════════════════════════════════════╣
║ PHASE 2: Mid Game (100-600 XP)                               ║
║  • Enemies get stronger each wave                            ║
║  • Map starts zooming out                                    ║
║  • Collect powerups (Rapid Fire, Multi Shot, etc.)           ║
║  • Progress through Keep and Bombard Tower                   ║
╠═══════════════════════════════════════════════════════════════╣
║ PHASE 3: Late Game (600-1000 XP)                             ║
║  • Reach Castle status                                       ║
║  • Face increasingly difficult enemies                       ║
║  • Map fully zoomed out                                      ║
╠═══════════════════════════════════════════════════════════════╣
║ PHASE 4: BOSS FIGHT (1000+ XP)                               ║
║  • 🐉 DRAGON APPEARS!                                        ║
║  • Massive health pool (1000 HP)                             ║
║  • Defeat to win the game!                                   ║
╚═══════════════════════════════════════════════════════════════╝

✨ FANTASY ELEMENTS (Powerups):
┌───────────────────────────────────────────────────────────────┐
│ 🔵 Rapid Fire      - Shoot arrows much faster                │
│ 🟠 Multi Shot      - Fire multiple arrows at once            │
│ 🟣 Piercing Arrows - Arrows go through multiple enemies      │
│ 🔷 Shield          - Temporary invulnerability               │
└───────────────────────────────────────────────────────────────┘

💎 LOOT SYSTEM:
┌───────────────────────────────────────────────────────────────┐
│ 🟡 XP Orbs         - Extra experience points                 │
│ 🟢 Health Orbs     - Restore health (future)                 │
│ 🟠 Damage Orbs     - Increase arrow damage (future)          │
│                                                               │
│ Drop Rates:                                                   │
│  • Loot: 20% chance per enemy                                │
│  • Powerups: 10% chance per enemy                            │
└───────────────────────────────────────────────────────────────┘

🎯 COMBAT MECHANICS:
• Click anywhere to shoot an arrow in that direction
• Arrows automatically seek the clicked position
• Each arrow deals 20 base damage
• Enemies have health bars showing their status
• Defeat enemies before they reach your position!

📊 WAVE SYSTEM:
• Wave 1: 5 enemies  (50 HP each)
• Wave 2: 7 enemies  (60 HP each)
• Wave 3: 9 enemies  (70 HP each)
• ... enemies increase in number and strength
• New waves spawn after a 5-second delay

🐉 DRAGON BOSS:
┌───────────────────────────────────────────────────────────────┐
│ Health:  1000 HP (50x stronger than basic enemies)           │
│ Speed:   30 (slower but more menacing)                       │
│ Damage:  50 (devastating if it reaches you)                  │
│ Special: Larger sprite with wings, unique purple/orange      │
│ Victory: Defeat the dragon to win the game!                  │
└───────────────────────────────────────────────────────────────┘

🎨 VISUAL PROGRESSION:
As you upgrade buildings, you'll see:
• Base Camp: Small brown tent
• Archer Tower: Stone tower with pointed roof
• Keep: Fortified structure with battlements
• Bombard Tower: Dark tower with cannons
• Castle: Full medieval castle with towers and gate

🖼️  SCREEN LAYOUT:
┌────────────────────────────────────────────────────────────────┐
│ XP: 450                               Wave: 5                  │
│ Building: Keep                                                 │
│ Next: Bombard Tower (150 XP needed)                           │
│                                                                │
│                        [Dragon Indicator]                      │
│                                                                │
│              🏰                    👹                          │
│                       ▲ (You)        ⚫ (Enemy)                │
│                                                                │
│                  ⚫                                             │
│                              ⚫                                 │
│                                                                │
│ WASD: Move | Click: Shoot                                     │
└────────────────────────────────────────────────────────────────┘

💡 TIPS & STRATEGIES:
1. Keep moving! Don't let enemies surround you
2. Prioritize enemies closest to your position
3. Collect all loot before it disappears (10s timer)
4. Save powerups for tougher waves
5. The map zooms out - be aware of enemies from all directions
6. Build up XP gradually - rushing leads to being overwhelmed
7. Practice your aim - click ahead of moving enemies

🏆 WIN CONDITION:
Defeat the Dragon Boss that appears at 1000 XP!

💀 LOSE CONDITION:
Any enemy touches the player character

════════════════════════════════════════════════════════════════

🚀 READY TO PLAY?

Run the game with:
    python main.py

Run tests with:
    python test_gameplay.py

════════════════════════════════════════════════════════════════
""")
