"""One-emoji entry for the make.fun bounty 'One Emoji, One Smile'.

Writes exactly one emoji and nothing else to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.

Round 3 entry: U+1F436 DOG FACE -- a friendly puppy face. (Round 2 was
the sunflower, U+1F33B; round 1 the sun with face, U+1F31E.) A dog's face
is the warmest first-glance pick of all: almost everyone smiles at a
puppy, whatever their age or background, with no context needed and no
words attached. It carries no intimacy, sarcasm or flirtation, so it works
coming from someone unknown, and unlike a smiley it is a living creature
looking back at you -- the warmth is in the face itself, not in a symbol
of a smile. A plain smiley would have been the obvious default; the dog
is the deliberate choice, and the same glyph reads the same way in every
locale, on every phone.

Entry rules enforced here: the bounty asks for exactly one emoji, so the
gate below is 1-8 characters -- one emoji character, with the 8-character
ceiling as the bounty's own allowance for multi-codepoint emoji -- and the
entry file contains that single emoji and nothing else, not even a newline.
"""

import os

EMOJI = "\U0001F436"


def main() -> None:
    # One-emoji gate: exactly one emoji character (len == 1 here), inside the
    # bounty's 1-8 character allowance, and not whitespace-only, so the entry
    # file holds a single visible emoji and nothing else.
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"
    assert EMOJI.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
