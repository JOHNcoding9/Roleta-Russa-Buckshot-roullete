# 🔫 BuckShot Roullete
**Buckshot Roullete** is a Python terminal game for two players. The mechanics include randomness, sound effects, and deadly decisions. Choose to shoot **yourself** (for a chance at an extra turn) or your **opponent** (for a faster victory).

---

## ⚙️ Features

- 🔫 Randomly generated chamber count (between 10 and 20)
- 💣 Random number of loaded chambers (with safety constraints)
- 🎮 Two-player local turn-based gameplay
- 🎵 Sound effects using `pygame`:
  - Trigger pull
  - Gunshot
- 💀 Real-time death chance percentage displayed
- 🎯 Extra turn mechanic for "shooting yourself"

---

## 🛠️ Requirements

- Python 3.x
- [`pygame`](https://pypi.org/project/pygame/)



## 🎮 How to Play

Run the game:

1.Enter player names when prompted.

2.The game will display:
  * Total number of chambers
  * Number of loaded chambers
  * Death probability (%)
  * Loaded chambers (After game's end only)

3.On each turn, the player chooses:

 * Whether to shoot "em si" (yourself) or "oponente" (your opponent)

 * A chamber number to fire

 * If the chamber is loaded:
   The target dies, and the game ends.

 * If not:
   The game continues to the next turn.

4.If you chose "em si", you get an extra turn next round.


## 🔊 Audio Files Required
Place the following audio files in the same directory as the script:

fgatilho.mp3 – Sound of pulling the trigger

Gunshot.mp3 – Gunshot sound

Make sure these files are valid and not empty. Otherwise, pygame will throw a runtime error.

##🧠 Strategy Hint
Shooting yourself can be a risk, but if you survive, you get an extra turn.

The chance of death is always displayed — use it wisely.
