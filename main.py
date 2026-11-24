"""One-emoji entry for the make.fun bounty 'One Emoji, One Smile'.

Writes exactly one emoji and nothing else to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.

Round 2 entry: U+1F33B SUNFLOWER -- a bright sunflower. (Round 1 was the
sun with face, U+1F31E.) A stranger glancing at a phone screen reads
sunshine at first glance: sunflowers are universally cheerful across ages
and backgrounds, warm and friendly with no context needed, a deliberately
chosen pick rather than the first default smiley, and they carry no
intimacy, sarcasm or flirtation, so the pick works coming from someone
unknown. A sunflower smiles without a face at all -- the cheerfulness
comes from the flower itself, so nothing in it can be read as smug, flirty
or mocking. A plain smiley would have been the obvious default; the
sunflower is the deliberate choice, and the same glyph reads the same way
in every locale, on every phone.

Entry rules enforced here: the bounty asks for exactly one emoji, so the
gate below is 1-8 characters -- one emoji character, with the 8-character
ceiling as the bounty's own allowance for multi-codepoint emoji -- and the
entry file contains that single emoji and nothing else, not even a newline.
"""

import os

EMOJI = "\U0001F33B"


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
