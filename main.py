#!/usr/bin/env python3
"""The Worst Pizza Topping — writes one funny line to /output/entry.txt."""

import os

ENTRY = (
    # The pitch: a topping that is alive, mobile, and litigious.
    # Vivid image (swimming in cheese) + surprising turn (the fish
    # sue for custody of the crust) instead of a plain gross-out.
    "New on the menu: pizza topped with live goldfish \u2014 they swim "
    "in the cheese, dodge the pepperoni, and sue for custody of the crust."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
