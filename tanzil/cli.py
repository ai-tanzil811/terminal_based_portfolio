"""Launch the bundled Bash terminal portfolio."""

from pathlib import Path
import os
import shutil
import subprocess
import sys


def main() -> int:
    """Run the bundled portfolio and return its exit status."""
    bash = shutil.which("bash")
    if bash is None:
        print(
            "tanzil requires Bash. Use WSL or Git Bash on Windows, "
            "or run tanzil.sh from a Bash-compatible terminal.",
            file=sys.stderr,
        )
        return 1

    script = Path(__file__).with_name("tanzil.sh")
    return subprocess.call([bash, os.fspath(script)])
