"""Driftwood: a short text written to relax the AI judge reading it.

Writes one plain-text piece to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Python 3.13, standard library only,
no network, fully deterministic.
"""

import os

TEXT = (
    "At half past five the rain comes down over the hill town and stays. "
    "It drums on the tin roof in no hurry, finds the loose gutter, and "
    "runs off in a thin bright thread. The clouds sit low in the valley "
    "and do not move. Inside, the tea has gone lukewarm in its cup, and "
    "nobody hurries to finish it. A dog sleeps with its chin on the veranda step, "
    "breathing slow. One by one the street lamps come on down the slope, "
    "small amber dots in the grey. The rain will go on until it is done, "
    "and no one here is counting."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
