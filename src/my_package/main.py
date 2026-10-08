"""Interactive terminal portfolio for Ashraful Islam Tanzil (AI Tanzil).

A small, dependency-free terminal app that presents a portfolio and a
collection of mini-games. Runs on any ANSI-capable terminal.
"""

from __future__ import annotations

import argparse
import os
import random
import sys
import time
from dataclasses import dataclass
from typing import Callable, Dict, Sequence

# --------------------------------------------------------------------------- #
# Profile data
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Profile:
    name: str
    handle: str
    tagline: str
    bio: str
    email: str
    github: str
    linkedin: str
    twitter: str
    website: str
    live_project: str
    huggingface: str
    kaggle: str
    dataset: str
    figma: str
    photo: str

    @property
    def mailto(self) -> str:
        return f"mailto:{self.email}"

    @property
    def greenpeft_model(self) -> str:
        return f"{self.huggingface}/GreenPEFT"


ME = Profile(
    name="Ashraful Islam Tanzil",
    handle="ai-tanzil811",
    tagline="CS undergraduate | AI & Cybersecurity | Bioinformatics Researcher",
    bio=(
        "I am a computer science undergraduate with a strong interest in "
        "artificial intelligence, cybersecurity, and bioinformatics. I have "
        "worked on various projects, including the development of a multi-objective "
        "Green AI decision support framework called GreenPEFT, which aims to "
        "optimize AI models for energy efficiency and performance. I am passionate "
        "about learning new technologies and applying them to solve real-world "
        "problems. I am also an active contributor to open-source projects and enjoy "
        "sharing my knowledge with the community through my portfolio and social media "
        "channels."        
    ),
    email="ahmedtanzil174@gmail.com",
    github="https://github.com/ai-tanzil811",
    linkedin="https://www.linkedin.com/in/ai-tanzil/",
    twitter="https://x.com/ai_tanzil",
    website="https://ai-tanzil811.github.io/PORTFOLIO2/",
    live_project="https://green-peft.vercel.app/",
    huggingface="https://huggingface.co/ai-tanzil",
    kaggle="https://www.kaggle.com/ashrafulislamtanzil",
    dataset="https://www.kaggle.com/datasets/ashrafulislamtanzil/greenpeft-surrogate-data",
    figma="https://www.figma.com/community/file/1623757181053559103/medivault",
    photo="https://gravatar.com/crownelectronic4c6790a6af",
)

BANNER = r"""
   █████╗ ██╗    ████████╗ █████╗ ███╗   ██╗███████╗██╗██╗
  ██╔══██╗██║    ╚══██╔══╝██╔══██╗████╗  ██║╚══███╔╝██║██║
  ███████║██║       ██║   ███████║██╔██╗ ██║  ███╔╝ ██║██║
  ██╔══██║██║       ██║   ██╔══██║██║╚██╗██║ ███╔╝  ██║██║
  ██║  ██║██║       ██║   ██║  ██║██║ ╚████║███████╗██║███████╗
  ╚═╝  ╚═╝╚═╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝╚══════╝
"""


# --------------------------------------------------------------------------- #
# Colors (enabled by default; respects NO_COLOR and --no-color)
# --------------------------------------------------------------------------- #


@dataclass
class Colors:
    RESET: str = "\033[0m"
    BOLD: str = "\033[1m"
    DIM: str = "\033[2m"
    CYAN: str = "\033[36m"
    MAGENTA: str = "\033[35m"
    GREEN: str = "\033[32m"
    YELLOW: str = "\033[33m"
    RED: str = "\033[31m"

    def disable(self) -> None:
        for name in vars(self):
            setattr(self, name, "")


C = Colors()


# --------------------------------------------------------------------------- #
# Terminal primitives
# --------------------------------------------------------------------------- #


def is_interactive() -> bool:
    return sys.stdin.isatty() and sys.stdout.isatty()


def clear_screen() -> None:
    """Clear the terminal and move the cursor home."""
    if is_interactive():
        print("\033[2J\033[H", end="")
    else:
        print()


def pause() -> None:
    """Wait for the user to press Enter."""
    if not is_interactive():
        return
    try:
        input(f"\n{C.DIM}Press Enter to continue...{C.RESET}")
    except (EOFError, KeyboardInterrupt):
        print()


def ask(prompt: str = "> ") -> str:
    """Read a line from stdin. Returns 'q' on EOF."""
    try:
        return input(prompt)
    except EOFError:
        print()
        return "q"


def is_quit(value: str) -> bool:
    return value.strip().lower() in {"q", "quit", "exit"}


def link(label: str, url: str) -> str:
    """Return an OSC 8 terminal hyperlink with a visible URL fallback."""
    return f"\033]8;;{url}\a{label}\033]8;;\a ({url})"


def type_line(text: str, delay: float = 0.012) -> None:
    """Print text one character at a time."""
    if os.environ.get("TANZIL_NO_ANIMATION") == "1":
        print(text)
        return
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def header() -> None:
    clear_screen()
    print(f"{C.CYAN}{C.BOLD}{BANNER}{C.RESET}")
    print(f"{C.DIM}  AI Tanzil • terminal portfolio • {ME.handle}{C.RESET}\n")


# --------------------------------------------------------------------------- #
# Page decorator — removes the header/print/pause boilerplate
# --------------------------------------------------------------------------- #


def page(title: str) -> Callable[[Callable[[], None]], Callable[[], None]]:
    def deco(fn: Callable[[], None]) -> Callable[[], None]:
        def wrapper() -> None:
            header()
            print(f"{C.BOLD}{C.MAGENTA}{title}{C.RESET}\n")
            fn()
            pause()

        wrapper.__name__ = fn.__name__
        wrapper.__doc__ = fn.__doc__
        return wrapper

    return deco


# --------------------------------------------------------------------------- #
# Portfolio pages
# --------------------------------------------------------------------------- #


@page("ABOUT")
def about() -> None:
    type_line(ME.tagline)
    print(f"\n\n{ME.bio}\n")
    print(f"{C.BOLD}Focus{C.RESET}")
    print("  React.js, full-stack web development, machine learning, and AI.")
    print(f"\n{C.BOLD}Profiles{C.RESET}")
    print(f"  {link('GitHub', ME.github)}")
    print(f"  {link('LinkedIn', ME.linkedin)}")
    print(f"  {link('Email', ME.mailto)}")
    print(f"  {link('Profile photo', ME.photo)}")


@page("PROJECTS & RESEARCH")
def projects() -> None:
    entries = (
        (
            "GreenPEFT",
            "Multi-objective Green AI decision support framework.",
            (
                ("Live", ME.live_project, ME.live_project),
                ("Model", ME.greenpeft_model, ME.greenpeft_model),
            ),
            "active / published",
        ),
        (
            "GreenPEFT surrogate data",
            "Dataset supporting the GreenPEFT research work.",
            (("Dataset", ME.dataset, ME.dataset),),
            None,
        ),
        (
            "MediVault UI/UX",
            "Community UI/UX design concept.",
            (("Figma", ME.figma, ME.figma),),
            None,
        ),
        (
            "Portfolio website",
            "Personal site and project index.",
            (("Website", ME.website, ME.website),),
            None,
        ),
    )
    for i, (name, blurb, links, status) in enumerate(entries):
        if i:
            print()
        print(f"{C.GREEN}{name}{C.RESET}")
        print(f"  {blurb}")
        for label, text, url in links:
            print(f"  {label + ':':<8}{link(text, url)}")
        if status:
            print(f"  Status: {status}")


@page("SKILLS")
def skills() -> None:
    rows = (
        ("Languages", "Python, JavaScript, HTML, CSS, C, C++"),
        ("Frameworks", "React, Node.js"),
        ("Tools", "Git, VS Code, npm"),
        ("Databases", "MySQL"),
        ("Platforms", "Kaggle, Hugging Face"),
    )
    for label, value in rows:
        print(f"{C.CYAN}{label + ':':<12}{C.RESET}{value}")
    print(f"\nKaggle: {link(ME.kaggle, ME.kaggle)}")


@page("CONTACT")
def contact() -> None:
    rows = (
        ("Email", "Email", ME.mailto),
        ("GitHub", ME.github, ME.github),
        ("LinkedIn", ME.linkedin, ME.linkedin),
        ("X", ME.twitter, ME.twitter),
        ("Website", ME.website, ME.website),
    )
    for label, display, url in rows:
        print(f"{label + ':':<10}{link(display, url)}")


# --------------------------------------------------------------------------- #
# Menu helper
# --------------------------------------------------------------------------- #


def run_menu(
    prompt: str,
    options: Dict[str, Callable[[], None]],
    *,
    on_invalid: Callable[[], None] | None = None,
) -> None:
    """Prompt once, dispatch to the chosen action, ignore quit/empty."""
    choice = ask(prompt).strip().lower()
    if is_quit(choice) or choice == "":
        return
    action = options.get(choice)
    if action is None:
        print(f"{C.YELLOW}Invalid choice.{C.RESET}")
        (on_invalid or (lambda: time.sleep(0.6)))()
        return
    action()


def play_again() -> bool:
    """Ask whether to replay. Returns True only on 'r'."""
    choice = ask(
        f"\n{C.DIM}[r]{C.RESET} Play again  "
        f"{C.DIM}[m]{C.RESET} Games menu  "
        f"{C.DIM}[q]{C.RESET} Main menu\n> "
    ).strip().lower()
    return choice == "r"


# --------------------------------------------------------------------------- #
# Games
# --------------------------------------------------------------------------- #


def guess_number() -> None:
    while True:
        header()
        print(f"{C.BOLD}{C.MAGENTA}GUESS THE NUMBER{C.RESET}\n")
        print("Guess a number from 1 to 20. [q] quit\n")
        target, tries = random.randint(1, 20), 0
        while True:
            value = ask()
            if is_quit(value):
                return
            try:
                guess = int(value)
            except ValueError:
                print(f"{C.YELLOW}Enter a number between 1 and 20.{C.RESET}")
                continue
            if not 1 <= guess <= 20:
                print(f"{C.YELLOW}Enter a number between 1 and 20.{C.RESET}")
                continue
            tries += 1
            if guess == target:
                print(f"{C.GREEN}You won in {tries} tries!{C.RESET}")
                break
            print("Too low." if guess < target else "Too high.")
        if not play_again():
            return


def rps() -> None:
    names = ("", "Rock", "Paper", "Scissors")
    winning = {(1, 3), (2, 1), (3, 2)}
    while True:
        header()
        print(f"{C.BOLD}{C.MAGENTA}ROCK PAPER SCISSORS{C.RESET}\n")
        choice = ask("[1] Rock  [2] Paper  [3] Scissors  [q] Quit\n> ").strip()
        if is_quit(choice):
            return
        if len(choice) != 1 or choice not in "123":
            print(f"{C.YELLOW}Invalid choice.{C.RESET}")
            pause()
            continue
        player, computer = int(choice), random.randint(1, 3)
        print(f"You: {names[player]} | Computer: {names[computer]}")
        if player == computer:
            print("Draw!")
        elif (player, computer) in winning:
            print(f"{C.GREEN}You win!{C.RESET}")
        else:
            print("Computer wins.")
        if not play_again():
            return


WINNING_LINES: tuple[tuple[int, int, int], ...] = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def board_text(board: Sequence[str]) -> str:
    return (
        f" {board[0]} | {board[1]} | {board[2]}\n"
        "---+---+---\n"
        f" {board[3]} | {board[4]} | {board[5]}\n"
        "---+---+---\n"
        f" {board[6]} | {board[7]} | {board[8]}"
    )


def winner(board: Sequence[str]) -> bool:
    return any(board[a] == board[b] == board[c] for a, b, c in WINNING_LINES)


def tic_tac_toe() -> None:
    while True:
        board = list("123456789")
        result = ""
        while True:
            header()
            print(f"{C.BOLD}{C.MAGENTA}TIC-TAC-TOE{C.RESET}\n")
            print("You are X. Choose a numbered square. [q] quit\n")
            print(board_text(board))
            move = ask("\nYour move: ").strip()
            if is_quit(move):
                return
            try:
                index = int(move) - 1
            except ValueError:
                print(f"{C.YELLOW}Choose an available square from 1 to 9.{C.RESET}")
                time.sleep(0.8)
                continue
            if not 0 <= index <= 8 or board[index] != move:
                print(f"{C.YELLOW}Choose an available square from 1 to 9.{C.RESET}")
                time.sleep(0.8)
                continue
            board[index] = "X"
            if winner(board):
                result = "You win!"
                break
            available = [i for i, v in enumerate(board) if v.isdigit()]
            if not available:
                result = "Draw!"
                break
            board[random.choice(available)] = "O"
            if winner(board):
                result = "Computer wins."
                break
        header()
        print(f"{C.BOLD}{C.MAGENTA}TIC-TAC-TOE{C.RESET}\n\n{board_text(board)}")
        color = C.GREEN if result == "You win!" else C.RESET
        print(f"\n{color}{result}{C.RESET}")
        if not play_again():
            return


def hangman() -> None:
    words = ("python", "kernel", "matrix", "terminal", "science", "network", "coffee")
    max_wrong = 6
    while True:
        word = random.choice(words)
        guessed: set[str] = set()
        wrong = 0
        while True:
            header()
            display = " ".join(letter if letter in guessed else "_" for letter in word)
            print(f"{C.BOLD}{C.MAGENTA}HANGMAN{C.RESET}\n\nWord: {display}")
            print(
                f"Wrong: {wrong}/{max_wrong}   "
                f"Guessed: {''.join(sorted(guessed)) or 'none'}"
            )
            if all(letter in guessed for letter in word):
                print(f"\n{C.GREEN}You won! The word was {word}.{C.RESET}")
                break
            if wrong >= max_wrong:
                print(f"\n{C.RED}Out of tries. The word was {word}.{C.RESET}")
                break
            guess = ask("Guess a letter: ").strip().lower()
            if is_quit(guess):
                return
            if len(guess) != 1 or not guess.isalpha():
                print(f"{C.YELLOW}Enter a single letter.{C.RESET}")
                time.sleep(0.7)
                continue
            if guess in guessed:
                print(f"{C.YELLOW}Already guessed.{C.RESET}")
                time.sleep(0.7)
                continue
            guessed.add(guess)
            if guess not in word:
                wrong += 1
        if not play_again():
            return


def dice() -> None:
    while True:
        header()
        print(f"{C.BOLD}{C.MAGENTA}DICE ROLLER{C.RESET}\n")
        if is_quit(ask("Press Enter to roll, or q to return.\n> ")):
            return
        print(f"{C.GREEN}You rolled: {random.randint(1, 6)}{C.RESET}")
        if not play_again():
            return


def games() -> None:
    options: Dict[str, Callable[[], None]] = {
        "1": guess_number,
        "2": tic_tac_toe,
        "3": rps,
        "4": hangman,
        "5": dice,
    }
    while True:
        header()
        print(f"{C.BOLD}{C.MAGENTA}GAMES{C.RESET}\n")
        print("[1] Guess the Number\n[2] Tic-Tac-Toe\n[3] Rock Paper Scissors")
        print("[4] Hangman\n[5] Dice Roller\n[q] Main menu")
        run_menu("\nChoose an option ", options)


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Interactive terminal portfolio.")
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI colors.")
    parser.add_argument(
        "--no-animation",
        action="store_true",
        help="Disable the typewriter effect.",
    )
    return parser.parse_args()


def configure(args: argparse.Namespace) -> None:
    # Windows: enable ANSI in cmd.exe and modern PowerShell.
    if os.name == "nt":
        os.system("")
    if args.no_color or os.environ.get("NO_COLOR"):
        C.disable()
    if args.no_animation:
        os.environ["TANZIL_NO_ANIMATION"] = "1"


def main() -> int:
    """Run the portfolio until the user quits."""
    configure(parse_args())
    pages: Dict[str, Callable[[], None]] = {
        "1": about,
        "2": projects,
        "3": skills,
        "4": contact,
        "5": games,
    }
    try:
        while True:
            header()
            print(f"{C.BOLD}{ME.name}{C.RESET}\n{ME.tagline}\n")
            print(
                "[1] About\n[2] Projects\n[3] Skills\n"
                "[4] Contact\n[5] Games\n[q] Quit"
            )
            run_menu("\nChoose an option ", pages)
    except KeyboardInterrupt:
        return 130
    finally:
        print(f"{C.RESET}\033[?25h", end="")


if __name__ == "__main__":
    raise SystemExit(main())