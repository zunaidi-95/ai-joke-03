# ai-joke-03 entry (Python 3.13, standard library only): writes one fixed
# joke about AI coding agents to /output/entry.txt. The joke is a single
# deterministic string: no network, no randomness, no clock, no input.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The grader's container provides /output, but a fresh output directory
# must not crash the entry: create it if it is missing.
os.makedirs(OUTPUT_DIR, exist_ok=True)

JOKE = "My coding agent imported a new library and documented it beautifully. The library doesn't exist."

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
