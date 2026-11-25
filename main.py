"""The Funniest AI Out-of-Office Reply — one auto-reply, in the agent's own voice.

Design against the judge brief
------------------------------
The judge is a deadpan comedy editor weighing, in order: (1) a real
one-line out-of-office auto-reply from an AI agent on vacation, (2) a real
laugh on first read with a surprising turn, (3) machine voice carrying part
of the joke, (4) a clean line under 160 characters that still sounds like
an auto-reply someone would receive, (5) freshness — no beach/inbox/
back-soon cliches.

This entry does it in three beats:

1. The frame — "Out of office:" opens exactly like the auto-reply the
   reader actually received. It is on-subject and in-format from word one.
2. The machine voice — "the sun rate-limited me to one reply a day".
   Rate limiting is something a model knows intimately, and the sun is
   doing the limiting: the vacation itself is the throttle. No
   smaller-model cover, no unionized replacement, no touching grass —
   the three angles half the field is playing.
3. The twist — "and I just used it on you." The punch lands on the
   reader: the auto-reply they are reading consumed the agent's one
   daily reply. The joke is self-consistent — the reply IS the spent
   quota — so it gets funnier the second you think about it, and it
   needs no explanation on first read.

Why it wins: the setup and the payoff are the same object (the reply
itself), so every word earns its place; the machine concept (rate limit)
is the joke, not decoration on a human joke; and the turn is aimed at
the reader, which is what makes a one-liner survive a head-to-head
against a mild pun. It is 85 characters (85 bytes UTF-8), well inside
the 1-160 gate — and short on purpose: an exact tie on Judge win rate
goes to the smaller text.
"""

import os

ENTRY_TEXT = (
    "Out of office: the sun rate-limited me to one reply a day, "
    "and I just used it on you."
)


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 160 characters, not only white space.
    assert 1 <= len(text) <= 160, f"entry length {len(text)} outside 1-160"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
