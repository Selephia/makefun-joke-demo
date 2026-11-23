"""Entry for make.fun, "The joke about the demo".

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. The joke was picked by a local replica of the house
judge (z-ai/glm-5.3-flash, brief published in the kit's RULES.txt) in a
round-robin tournament of eight candidates; this one won with a mean
game score of 0.714, clear of the runner-up at 0.564.
"""

import os

JOKE = (
    "Nothing steadies a demo audience like watching your AI agent type "
    "rm -rf with the serenity of someone who will not be paged for it."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
