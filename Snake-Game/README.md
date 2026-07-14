# Snake Game

Classic Snake built with Python's Tkinter.

## Features
- Wraparound walls (no instant death at edges)
- Speed increases as you eat food
- Pause / Resume with Space
- Restart with R after Game Over
- Score tracker

## Requirements
- Python 3
- Tkinter (bundled with most Python installs)

## Run
```
python game.py
```

## Controls
| Key | Action |
|---|---|
| Arrow keys | Move |
| Space | Pause/Resume |
| R | Restart (after game over) |

## Structure
- `Snake` class — body segments, drawing
- `Food` class — random spawn, drawing
- `next_turn()` — game loop (movement, collision, growth)
- `check_collisions()` — self-collision detection