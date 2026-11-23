"""One-emoji entry for the make.fun bounty 'One Emoji, One Smile'.

Writes exactly one emoji and nothing else to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.

Chosen emoji: U+1F31E SUN WITH FACE -- a smiling sun. A stranger glancing
at a phone screen reads a warm face at first glance, and sunshine is
universally cheerful across ages and backgrounds: it is warm, friendly and
gently funny with no context needed, it is a deliberately chosen pick rather
than the first default smiley, and it carries no intimacy, sarcasm or
flirtation, so it works coming from someone unknown.

Why this emoji and not another face: the sun with a face pairs the smile
itself with sunshine, so the cheerfulness comes from the image, not from a
facial expression that could be read as smug, flirty or mocking. A plain
smiley would have been the obvious default; the sun is the deliberate
choice -- it smiles without asking anything of the reader, and the same
glyph reads the same way in every locale, on every phone.

Entry rules enforced here: the bounty asks for exactly one emoji, so the
gate below is 1-8 characters -- one emoji character, with the 8-character
ceiling as the bounty's own allowance for multi-codepoint emoji -- and the
entry file contains that single emoji and nothing else, not even a newline.
"""

import os

EMOJI = "\U0001F31E"


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
