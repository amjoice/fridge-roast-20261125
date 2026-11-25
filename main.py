"""Fridge Roast: One Line, Biggest Laugh (make.fun).

Writes a single roast of a smart fridge — at most 200 characters — to
/output/entry.txt, where the house judge reads it.

The line targets the fridge's app treating groceries like a phone
battery: a freshness percentage for milk. It is a roast of the app
itself, it is specific to smart fridges (no other appliance reports
a freshness percentage), every word earns its place, and it dodges
the obvious cracks about ordering groceries or watching you.
"""

import os

LINE = "My fridge says my milk is at 12%. Twelve percent of what — hope? It's milk, not a phone battery. Stop giving my groceries a health bar."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_DIR}/entry.txt")


if __name__ == "__main__":
    main()
