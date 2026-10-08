
For each game:

1. Must be fully playable with keyboard input only.
2. Must be self-contained in the same script (no external files unless optional).
3. Must handle invalid input without crashing.
4. Must have a clear win/lose/draw state.
5. Must allow the player to quit back to the Games menu at any time by pressing `q` or `Esc`.
6. Must use `/dev/tty` for input if the script was piped via `curl | bash`.
7. Keep animations lightweight so it works in Termux and slow terminals.
8. Save nothing to disk unless I ask. No high-score files by default.

**Game selection rules:**
- If I did not specify games, pick a default set: Guess the Number, Tic-Tac-Toe, Rock-Paper-Scissors, and Dice Roller.
- If a game is too heavy for pure Bash (like Snake), either:
  - Implement it with `read -t` and a redraw loop, or
  - Port that one game to Python and explain the tradeoff.

**Controls (universal):**
- Arrow keys optional. If hard to detect, use `w/a/s/d` or number keys.
- Always show the controls on screen before the game starts.
- Always show a `[q] Quit` hint.

**Game exit flow:**
- After a game ends, show: `[r] Play again  [m] Games menu  [q] Main menu`.
- Never drop the user out of the program unexpectedly.

---

## OUTPUT FORMAT

1. Brief plan of what you will build, including the game list.
2. Full script in one code block.
3. How to run it locally.
4. How to host it as a `curl` one-liner.
5. How to host it as an SSH portfolio using `ForceCommand`.
6. Customization tips: how to change colors, ASCII art, animation speed, menu items, and how to add or remove games.
7. A short list of terminal compatibility notes.
8. A short note on which games work best in pure Bash vs. which may need Python.

Now generate the terminal portfolio with games from my data above.

If any required field is missing, ask me for it before generating the final code.