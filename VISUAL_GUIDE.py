#!/usr/bin/env python3
"""
Create a visual representation of the game at different stages
This generates text-based "screenshots" showing game progression
"""

print("""
════════════════════════════════════════════════════════════════════════
MEDIEVAL FANTASY DEFENSE - VISUAL PROGRESSION
════════════════════════════════════════════════════════════════════════

STAGE 1: EARLY GAME (Base Camp)
────────────────────────────────────────────────────────────────────────
┌──────────────────────────────────────────────────────────────────────┐
│ XP: 25                                          Wave: 1              │
│ Building: Base Camp                                                  │
│ Next: Archer Tower (75 XP needed)                                   │
│                                                                      │
│                          ┌─┐                                        │
│                         /   \\     <-- Base Camp (tent)              │
│                        /     \\                                       │
│                       └───────┘                                      │
│                                                                      │
│                    ▲         →→     <-- Arrow                       │
│                 (Archer)                                             │
│                                                                      │
│              ●  ●                  <-- Enemies approaching           │
│                     ●                                                │
│                                                                      │
│ WASD: Move | Click: Shoot                                           │
└──────────────────────────────────────────────────────────────────────┘

STAGE 2: MID GAME (Archer Tower)
────────────────────────────────────────────────────────────────────────
┌──────────────────────────────────────────────────────────────────────┐
│ XP: 225                                         Wave: 3              │
│ Building: Archer Tower                                               │
│ Next: Keep (75 XP needed)                                           │
│                                                                      │
│                          ╔═╗                                        │
│                          ║░║     <-- Archer Tower                   │
│                          ║░║                                         │
│                          ╚═╝                                        │
│                    ✦                  <-- Powerup                    │
│                ▲                                                     │
│             (Archer)  →→                                             │
│                                                                      │
│       ●         ●                                                    │
│  ●       ○            ●        <-- More enemies, some with loot     │
│                                                                      │
│ WASD: Move | Click: Shoot                                           │
└──────────────────────────────────────────────────────────────────────┘

STAGE 3: LATE GAME (Castle) - ZOOMED OUT
────────────────────────────────────────────────────────────────────────
┌──────────────────────────────────────────────────────────────────────┐
│ XP: 985                                         Wave: 12             │
│ Building: Castle                                                     │
│ Next: Dragon Fight Soon!                                            │
│                                                                      │
│                      ╔══╗  ╔══╗                                     │
│                      ║▓▓║  ║▓▓║  <-- Castle towers                  │
│                      ╠══╬══╬══╣                                     │
│     ●                ║▓▓▓▓▓▓▓▓║                                     │
│                      ╚════════╝                                     │
│  ●    ○    ●                                                         │
│         ▲    →→                                                      │
│  ●   (You)         ●                                                 │
│                                                                      │
│         ●    ✦    ●    ●    <-- Many enemies, loot scattered        │
│                                                                      │
│ WASD: Move | Click: Shoot                                           │
└──────────────────────────────────────────────────────────────────────┘

STAGE 4: DRAGON BOSS FIGHT
────────────────────────────────────────────────────────────────────────
┌──────────────────────────────────────────────────────────────────────┐
│ XP: 1050                                        Wave: 15             │
│ Building: Castle                                                     │
│                                                                      │
│                   ╔═ DRAGON BOSS! ═╗                                │
│                                                                      │
│                      ╔══╗  ╔══╗                                     │
│                      ║▓▓║  ║▓▓║                                     │
│       /\\~/\\        ╠══╬══╬══╣                                    │
│      (◉ ◉)  \\      ║▓▓▓▓▓▓▓▓║   <-- Dragon approaching!           │
│       \\_▼_/  )      ╚════════╝                                     │
│         │   /                                                        │
│        /│\\  Dragon                                                  │
│       ━━┻━━  HP: ████████░░ 800/1000                                │
│                                                                      │
│            ▲    →→→→                                                 │
│         (Archer)  <-- Multiple arrows needed!                       │
│                                                                      │
│              ✦         ○                                             │
│ WASD: Move | Click: Shoot                                           │
└──────────────────────────────────────────────────────────────────────┘

VICTORY SCREEN
────────────────────────────────────────────────────────────────────────
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│                                                                      │
│                                                                      │
│                  ╔═══════════════════════════╗                      │
│                  ║                           ║                      │
│                  ║  VICTORY! Dragon Defeated!║                      │
│                  ║                           ║                      │
│                  ║     Final XP: 1150        ║                      │
│                  ║                           ║                      │
│                  ║   Close window to exit    ║                      │
│                  ║                           ║                      │
│                  ╚═══════════════════════════╝                      │
│                                                                      │
│                          🏆 WINNER 🏆                                │
│                                                                      │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════

LEGEND:
  ▲     - Your archer
  ●     - Enemies (red circles in actual game)
  ○     - Loot drops (yellow/green/orange orbs)
  ✦     - Powerups (blue/orange/purple/cyan diamonds)
  →     - Arrows in flight
  
BUILDING PROGRESSION (as they appear in-game):
  Base Camp       - Brown tent
  Archer Tower    - Gray stone tower with pointed roof
  Keep            - Large fortified structure with battlements
  Bombard Tower   - Dark tower with cannons
  Castle          - Full medieval castle with towers and gate

ZOOM EFFECT:
Notice how the view gets wider from Stage 1 to Stage 3. This is the
zoom-out mechanic - you can see more of the battlefield as you upgrade!

════════════════════════════════════════════════════════════════════════
""")
