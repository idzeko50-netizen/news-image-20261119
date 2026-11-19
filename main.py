"""News-image entry for 19 November 2026.

Copies the image held in this repository to the grader's output
directory. Standard library only, no network, deterministic:
every run writes the same bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main() -> None:
    # The output file name stays entry.png even though the bytes are JPEG;
    # RULES.txt allows either format under that name.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")


if __name__ == "__main__":
    main()
