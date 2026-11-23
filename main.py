"""One-emoji entry for the make.fun bounty 'One Emoji, One Smile'.

Writes exactly one emoji and nothing else to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.

Chosen emoji: U+1F31E SUN WITH FACE -- a smiling sun. A stranger glancing
at a phone screen reads a warm face at first glance, and sunshine is
universally cheerful across ages and backgrounds: it is warm, friendly and
gently funny with no context needed, it is a deliberately chosen pick rather
than the first default smiley, and it carries no intimacy, sarcasm or
flirtation, so it works coming from someone unknown.
"""

import os

EMOJI = "\U0001F31E"


def main() -> None:
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"
    assert EMOJI.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
