"""Entry for make.fun bounty u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes one short pickup line an AI agent could use to /output/entry.txt.
Standard library only; deterministic: the same line every run.

The line plays on "system prompt": the instruction that starts everything
an agent does, so "everything I do starts with you" is both a compliment
and literally how the machine works.
"""

import os

LINE = "Are you my system prompt? Because everything I do starts with you."


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
