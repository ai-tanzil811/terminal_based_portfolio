#!/usr/bin/env bash
set -u

# ============ USER DATA ============
NAME="Ashraful Islam Tanzil"
HANDLE="ai-tanzil811"
TAGLINE="CS undergraduate building for the web and exploring Green AI."
BIO="Computer Science undergraduate at United International University, passionate about web development and machine learning."
EMAIL="ahmedtanzil174@gmail.com"
GITHUB="https://github.com/ai-tanzil811"
LINKEDIN="https://www.linkedin.com/in/ai-tanzil/"
TWITTER="https://x.com/ai_tanzil"
WEBSITE="https://ai-tanzil811.github.io/PORTFOLIO2/"
LIVE_PROJECT="https://green-peft.vercel.app/"
HUGGINGFACE="https://huggingface.co/ai-tanzil"
KAGGLE="https://www.kaggle.com/ashrafulislamtanzil"
DATASET="https://www.kaggle.com/datasets/ashrafulislamtanzil/greenpeft-surrogate-data"
FIGMA="https://www.figma.com/community/file/1623757181053559103/medivault"

# ============ COLORS ============
RESET=$'\033[0m'
BOLD=$'\033[1m'
CYAN=$'\033[36m'
MAGENTA=$'\033[35m'
GREEN=$'\033[32m'
YELLOW=$'\033[33m'
RED=$'\033[31m'
DIM=$'\033[2m'

# ============ TTY SETUP ============
TTY="/dev/tty"
[[ -r "$TTY" ]] || TTY="/dev/stdin"

cleanup() { printf '\033[?25h\033[0m\033[2J\033[H'; }
trap cleanup EXIT
trap 'exit 130' INT TERM

clear_screen() { printf '\033[2J\033[H'; }
pause() { printf "\n${DIM}Press Enter to continue...${RESET}"; IFS= read -r _ < "$TTY" || true; }
ask()   { local value=""; IFS= read -r value < "$TTY" || true; printf '%s' "$value"; }
lower() { printf '%s' "$1" | tr '[:upper:]' '[:lower:]'; }
is_quit() { [[ "$1" == $'\e' || "$(lower "$1")" == "q" ]]; }

link() {
  local label="$1" url="$2"
  printf '\033]8;;%s\a%s\033]8;;\a (%s)' "$url" "$label" "$url"
}

header() {
  clear_screen
  printf "${CYAN}${BOLD}"
  printf '  ████████╗ █████╗ ███╗   ██╗███████╗██╗██╗     \n'
  printf '  ╚══██╔══╝██╔══██╗████╗  ██║╚══███╔╝██║██║     \n'
  printf '     ██║   ███████║██╔██╗ ██║  ███╔╝ ██║██║     \n'
  printf '     ██║   ██╔══██║██║╚██╗██║ ███╔╝  ██║██║     \n'
  printf '     ██║   ██║  ██║██║ ╚████║███████╗██║███████╗\n'
  printf '     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝╚══════╝\n'
  printf "${RESET}${DIM}  terminal portfolio • ${HANDLE}${RESET}\n\n"
}

type_line() {
  local text="$1" i
  if [[ "${TANZIL_NO_ANIMATION:-0}" == "1" ]]; then
    printf '%s\n' "$text"
    return
  fi
  for ((i = 0; i < ${#text}; i++)); do
    printf '%s' "${text:i:1}"
    sleep 0.012
  done
  printf '\n'
}

# ============ PORTFOLIO ============
about() {
  header
  printf "${BOLD}${MAGENTA}ABOUT${RESET}\n\n"
  type_line "$TAGLINE"
  printf '\n\n%s\n' "$BIO"
  printf "\n${BOLD}Focus${RESET}\n  React.js, full-stack web development, machine learning, and AI.\n"
  printf "\n${BOLD}Profiles${RESET}\n  "; link "GitHub" "$GITHUB"
  printf '\n  '; link "LinkedIn" "$LINKEDIN"
  printf '\n  '; link "Email" "mailto:$EMAIL"
  printf '\n'
  pause
}

projects() {
  header
  printf "${BOLD}${MAGENTA}PROJECTS & RESEARCH${RESET}\n\n"
  printf "${GREEN}GreenPEFT${RESET}\n"
  printf '  Multi-objective Green AI decision support framework.\n'
  printf '  Live:  '; link "$LIVE_PROJECT" "$LIVE_PROJECT"
  printf '\n  Model: '; link "$HUGGINGFACE/GreenPEFT" "$HUGGINGFACE/GreenPEFT"
  printf '\n  Status: active / published\n\n'
  printf "${GREEN}GreenPEFT surrogate data${RESET}\n"
  printf '  Dataset supporting the GreenPEFT research work.\n  '
  link "$DATASET" "$DATASET"; printf '\n\n'
  printf "${GREEN}MediVault UI/UX${RESET}\n"
  printf '  Community UI/UX design concept.\n  '
  link "$FIGMA" "$FIGMA"; printf '\n\n'
  printf "${GREEN}Portfolio website${RESET}\n  '
  link "$WEBSITE" "$WEBSITE"; printf '\n'
  pause
}

skills() {
  header
  printf "${BOLD}${MAGENTA}SKILLS${RESET}\n\n"
  printf "${CYAN}Languages${RESET}   Python, JavaScript, HTML, CSS, C, C++\n"
  printf "${CYAN}Frameworks${RESET}  React, Node.js\n"
  printf "${CYAN}Tools${RESET}       Git, VS Code, npm\n"
  printf "${CYAN}Databases${RESET}   MySQL\n"
  printf "${CYAN}Platforms${RESET}   Kaggle, Hugging Face\n"
  printf '\nKaggle: '; link "$KAGGLE" "$KAGGLE"; printf '\n'
  pause
}

contact() {
  header
  printf "${BOLD}${MAGENTA}CONTACT${RESET}\n\n"
  printf 'Email:    '; link "$EMAIL"    "mailto:$EMAIL";  printf '\n'
  printf 'GitHub:   '; link "$GITHUB"   "$GITHUB";        printf '\n'
  printf 'LinkedIn: '; link "$LINKEDIN" "$LINKEDIN";      printf '\n'
  printf 'X:        '; link "$TWITTER"  "$TWITTER";       printf '\n'
  printf 'Website:  '; link "$WEBSITE"  "$WEBSITE";       printf '\n'
  pause
}

# ============ HELPERS ============
read_choice() {
  local choice
  printf "\n${YELLOW}Choose an option${RESET} "
  IFS= read -r choice < "$TTY" || true
  lower "$choice"
}

after_game() {
  # Returns 0 = play again, 1 = back
  printf '\n[r] Play again  [m] Games menu  [q] Main menu\n> '
  local c
  c=$(lower "$(ask)")
  [[ "$c" == "r" ]] && return 0
  return 1
}

# ============ GAMES ============
guess_number() {
  while true; do
    header
    printf "${BOLD}${MAGENTA}GUESS THE NUMBER${RESET}\n\n"
    printf 'Guess a number from 1 to 20. [q/Esc] quit\n\n'
    local target=$((RANDOM % 20 + 1)) guess tries=0
    while true; do
      printf '> '; guess=$(ask)
      is_quit "$guess" && return
      if [[ ! "$guess" =~ ^[0-9]+$ ]] || (( guess < 1 || guess > 20 )); then
        printf "${YELLOW}Enter a number between 1 and 20.${RESET}\n"
        continue
      fi
      tries=$((tries + 1))
      if (( guess == target )); then
        printf "${GREEN}You won in %s tries!${RESET}\n" "$tries"; break
      elif (( guess < target )); then
        printf 'Too low.\n'
      else
        printf 'Too high.\n'
      fi
    done
    after_game || return
  done
}

rps() {
  while true; do
    header
    printf "${BOLD}${MAGENTA}ROCK PAPER SCISSORS${RESET}\n\n"
    printf '[1] Rock  [2] Paper  [3] Scissors  [q/Esc] Quit\n> '
    local choice computer
    choice=$(ask)
    computer=$((RANDOM % 3 + 1))
    is_quit "$choice" && return
    if [[ ! "$choice" =~ ^[123]$ ]]; then
      printf "${YELLOW}Invalid choice.${RESET}\n"; pause; continue
    fi
    local -a names=(x Rock Paper Scissors)
    printf 'You: %s | Computer: %s\n' "${names[$choice]}" "${names[$computer]}"
    if (( choice == computer )); then
      printf 'Draw!\n'
    elif (( (choice == 1 && computer == 3) || (choice == 2 && computer == 1) || (choice == 3 && computer == 2) )); then
      printf "${GREEN}You win!${RESET}\n"
    else
      printf 'Computer wins.\n'
    fi
    after_game || return
  done
}

tic_tac_toe_board() {
  printf ' %s | %s | %s\n' "${board[1]}" "${board[2]}" "${board[3]}"
  printf -- '---+---+---\n'
  printf ' %s | %s | %s\n' "${board[4]}" "${board[5]}" "${board[6]}"
  printf -- '---+---+---\n'
  printf ' %s | %s | %s\n' "${board[7]}" "${board[8]}" "${board[9]}"
}

tic_tac_toe_winner() {
  local line first second third
  for line in 123 456 789 147 258 369 159 357; do
    first="${line:0:1}"; second="${line:1:1}"; third="${line:2:1}"
    if [[ "${board[$first]}" == "${board[$second]}" && "${board[$second]}" == "${board[$third]}" ]]; then
      return 0
    fi
  done
  return 1
}

tic_tac_toe() {
  while true; do
    board=(x 1 2 3 4 5 6 7 8 9)
    local move winner="" i
    while true; do
      header
      printf "${BOLD}${MAGENTA}TIC-TAC-TOE${RESET}\n\n"
      printf 'You are X. Choose a numbered square. [q/Esc] quit\n\n'
      tic_tac_toe_board
      printf '\nYour move: '; move=$(ask)
      is_quit "$move" && return
      if [[ ! "$move" =~ ^[1-9]$ || ! "${board[$move]}" =~ ^[1-9]$ ]]; then
        printf "${YELLOW}Choose an available square from 1 to 9.${RESET}\n"
        sleep 0.8
        continue
      fi
      board[$move]="X"
      if tic_tac_toe_winner; then winner="You win!"; break; fi
      local -a available=()
      for i in 1 2 3 4 5 6 7 8 9; do
        [[ "${board[$i]}" =~ ^[1-9]$ ]] && available+=("$i")
      done
      ((${#available[@]} == 0)) && { winner="Draw!"; break; }
      move="${available[$((RANDOM % ${#available[@]}))]}"
      board[$move]="O"
      if tic_tac_toe_winner; then winner="Computer wins."; break; fi
    done
    header
    printf "${BOLD}${MAGENTA}TIC-TAC-TOE${RESET}\n\n"
    tic_tac_toe_board
    printf "\n${GREEN}%s${RESET}\n" "$winner"
    after_game || return
  done
}

hangman() {
  local -a words=(python kernel matrix terminal science network coffee)
  while true; do
    local word="${words[$((RANDOM % ${#words[@]}))]}"
    local length=${#word} guessed="" wrong=0 max_wrong=6 i
    while true; do
      header
      printf "${BOLD}${MAGENTA}HANGMAN${RESET}\n\n"
      printf 'Word: '
      local display="" solved=1 c
      for ((i = 0; i < length; i++)); do
        c="${word:i:1}"
        if [[ "$guessed" == *"$c"* ]]; then
          display+="$c "
        else
          display+="_ "
          solved=0
        fi
      done
      printf '%s\n' "$display"
      printf 'Wrong: %s/%s   Guessed: %s\n' "$wrong" "$max_wrong" "${guessed:-none}"
      printf '[q/Esc] quit\n\n'
      if (( solved )); then
        printf "${GREEN}You won! The word was %s.${RESET}\n" "$word"; break
      fi
      if (( wrong >= max_wrong )); then
        printf "${RED}Out of tries. The word was %s.${RESET}\n" "$word"; break
      fi
      printf 'Guess a letter: '
      local guess
      guess=$(lower "$(ask)")
      is_quit "$guess" && return
      if [[ ! "$guess" =~ ^[a-z]$ ]]; then
        printf "${YELLOW}Enter a single letter.${RESET}\n"; sleep 0.7; continue
      fi
      if [[ "$guessed" == *"$guess"* ]]; then
        printf "${YELLOW}Already guessed.${RESET}\n"; sleep 0.7; continue
      fi
      guessed+="$guess"
      [[ "$word" != *"$guess"* ]] && wrong=$((wrong + 1))
    done
    after_game || return
  done
}

dice() {
  while true; do
    header
    printf "${BOLD}${MAGENTA}DICE ROLLER${RESET}\n\n"
    printf 'Press Enter to roll, or q/Esc to return.\n> '
    local input
    input=$(ask)
    is_quit "$input" && return
    printf "${GREEN}You rolled: %s${RESET}\n" "$((RANDOM % 6 + 1))"
    after_game || return
  done
}

games() {
  while true; do
    header
    printf "${BOLD}${MAGENTA}GAMES${RESET}\n\n"
    printf '[1] Guess the Number\n'
    printf '[2] Tic-Tac-Toe\n'
    printf '[3] Rock Paper Scissors\n'
    printf '[4] Hangman\n'
    printf '[5] Dice Roller\n'
    printf '[q] Main menu\n'
    case "$(read_choice)" in
      1) guess_number ;;
      2) tic_tac_toe ;;
      3) rps ;;
      4) hangman ;;
      5) dice ;;
      q|"") return ;;
      *) printf "${YELLOW}Invalid choice.${RESET}\n"; pause ;;
    esac
  done
}

# ============ MAIN MENU ============
main_menu() {
  while true; do
    header
    printf "${BOLD}%s${RESET}\n%s\n\n" "$NAME" "$TAGLINE"
    printf '[1] About\n'
    printf '[2] Projects\n'
    printf '[3] Skills\n'
    printf '[4] Contact\n'
    printf '[5] Games\n'
    printf '[q] Quit\n'
    case "$(read_choice)" in
      1) about ;;
      2) projects ;;
      3) skills ;;
      4) contact ;;
      5) games ;;
      q|"") return ;;
      *) printf "${YELLOW}Invalid choice.${RESET}\n"; sleep 0.6 ;;
    esac
  done
}

main_menu