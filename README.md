# HellTaker-Bot
I hated the final boss of the HellTaker DLC (ExamTaker), so I made a bot to destroy it but I ended up making a bot for the whole game.<br><br>
## ⚠️ If anyone from the game development team feels offended by this bot, I can remove it.

## Required Libraries

To run this script, it is necessary to install some Python libraries.

### Installation Instructions

1. **Keyboard**: This library is used to detect keyboard events.
   ```bash
   pip install keyboard

2. **Pygetwindow**: This library is used to find the window where Helltaker is running.
   ```bash
   pip install pygetwindow

3. **Pywin32**: This library is used to focus the Helltaker window and make sure to execute the key sequence in the game.
   ```bash
   pip install pywin32

## Compilation

### Run this python command inside the root directory to open the bot 
```
 python HellBot.py
```

# Use

1. Open Helltaker in windowed mode and open the bot. <br>
2. Start a new game or select a chapter. <br>
3. Click on the Helltaker or Examtaker button to see the list of levels and bosses.
4. At the beginning of the level press the corresponding button and the player will move automatically.<br>

  - 📌 **Notice** <br>
    - The bot only solves the puzzles and defeats the bosses, the narrative screens must be played manually <br>(The screen when picking up the Forbiden Lore piece is passed automatically)<br>
    - The Judegement or the final boss of Examtaker can be played completely automatically or just one of the stages in case you don't want so much help.
    - If you decide to press the Judgement Complete button and play all 4 phases in a row automatically, you will miss the plot as it will automatically skip the dialogues.

# GUI images

#### First Screen <br>

![First screen](https://github.com/maxborquez/HellTaker-Bot/blob/main/images/first%20screen.png) 

#### Click on the Helltaker or Examtaker button<br>

![HellTaker Screen](https://github.com/maxborquez/HellTaker-Bot/blob/main/images/helltaker%20screen.png) ![ExamTaker Screen](https://github.com/maxborquez/HellTaker-Bot/blob/main/images/examtaker%20screen.png)

# Thanks to

- No Frill Bear for part of its movement path for Judgment, phases 1,2,3 and 4.

  - https://www.youtube.com/watch?v=Qd156vVxiAc

- VFStudios for part of its movements path for the ExamTaker boss, phase 3.

  - https://www.youtube.com/watch?v=gUDS95q_Q2M
