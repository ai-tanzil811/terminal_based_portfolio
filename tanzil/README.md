# tanzil

Interactive, dependency-free terminal portfolio for Ashraful Islam Tanzil.

The project is also packaged as `tanzil` for PyPI. The package launches the bundled Bash portfolio.

## Build plan

The Bash program presents a compact profile, projects, skills, contact links, and a games menu using cyan/magenta ANSI styling, a lightweight typing effect, and OSC 8 links with visible URL fallbacks. The games are Guess the Number, Tic-Tac-Toe, Rock-Paper-Scissors, and Dice Roller.

The complete self-contained script is [`tanzil.sh`](./tanzil.sh).

## Run locally

```bash
chmod +x tanzil.sh
./tanzil.sh
```

Set `TANZIL_NO_ANIMATION=1` to disable typing animation:

```bash
TANZIL_NO_ANIMATION=1 ./tanzil.sh
```

## Host as a curl one-liner

Host `tanzil.sh` at a trusted HTTPS URL, then run:

```bash
curl -fsSL https://example.com/tanzil.sh | bash
```

The script reads interactive input from `/dev/tty` when available, so piping it does not consume menu input.

## Host as an SSH portfolio

Create a restricted account and add this to `~/.ssh/authorized_keys`:

```text
command="/path/to/tanzil.sh",no-agent-forwarding,no-port-forwarding,no-X11-forwarding,no-pty ssh-ed25519 AAAA...
```

Use a forced command wrapper if your SSH server does not provide a usable terminal path.

## Customization

Edit the profile constants at the top of `tanzil.sh` to change identity and links. Adjust the ANSI color constants, the `sleep` value in `type_line`, or add menu branches in `main_menu`. Games are implemented in the same script and can be added through `games`.

## Compatibility

- Works in Bash on Linux, macOS, Termux, WSL, and Git Bash.
- Uses basic ANSI colors and OSC 8 hyperlinks with plain URL fallbacks.
- No external runtime dependencies are required.
- A real terminal is recommended for keyboard interaction.

The default games are intentionally lightweight pure-Bash implementations. They do not save scores or require Python. Tic-Tac-Toe uses numbered squares 1–9; every game accepts `q` or Escape to leave, handles invalid input, and provides replay/menu choices after the game ends.

## Build and publish to PyPI

From a machine with Python packaging tools and PyPI credentials configured:

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine upload dist/*
```

Use a PyPI API token through Twine's supported credential configuration; do not place tokens in source files or commit `api.txt`.
