"""Entry for make.fun bounty "The Meeting That Should Have Been an Email".

Entry text (128 characters, limit: at most 200 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "We spent forty-five minutes in a meeting that could have been one email — mostly watching each other nod at a slide nobody read."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
