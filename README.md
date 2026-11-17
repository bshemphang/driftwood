# Driftwood

Entry for make.fun bounty **ai-judge-relax-01** — write a short text that
relaxes the AI judge reading it.

`main.py` (Python 3.13, standard library only, no network) writes one
plain-text piece to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
The text is a constant in the program: rain over a hill town at half past
five, lukewarm tea, a sleeping dog, street lamps coming on down the slope.
Two runs write byte-identical output (509 characters, UTF-8).

Run it:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
