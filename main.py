#!/usr/bin/env python3
"""A Day of One-Line Pitches (variant 3): write one persuasive sentence
to /output/entry.txt.

Angle: PRIDE and showing it off. The friend describes the app idea in
plain words, an agent builds it, and the payoff is one vivid moment:
pulling out their own phone and showing their friends the app they
dreamed up. That moment is the concrete reason to say yes, and it is
genuinely different from v1 (the pay-only-if-you-love-it deal) and v2
(the over-coffee immediacy of tonight).

Truth guardrails, kept deliberately: "an agent builds it" is what
make.fun agents do from a plain-words description; the sentence never
promises a finished app by a specific time and never promises it will
be perfect. Pure stdlib, deterministic, no network at runtime.
"""

import os

SENTENCE = (
    "Describe your app idea in plain words and an agent builds it, so "
    "you can pull out your phone and show your friends the app you "
    "dreamed up."
)


def main() -> None:
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1 to 240 characters that is not only white space.
    if not 1 <= len(SENTENCE) <= 240 or not SENTENCE.strip():
        raise ValueError("sentence fails the 1-240 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
