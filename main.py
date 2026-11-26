"""Write the one-line deadpan forecast to /output/entry.txt and verify it."""

import os

ENTRY = "Good evening from Tarnwick: an overnight low of 41, fog arriving on foot at 9 p.m., and a 70 percent chance it asks to be let in."

OUTPUT_PATHS = ["/output/entry.txt", "./output/entry.txt"]


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"

    written_path = None
    last_error = None
    for path in OUTPUT_PATHS:
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            written_path = path
            break
        except OSError as exc:  # e.g. /output not writable; try the fallback
            last_error = exc
    if written_path is None:
        raise RuntimeError(f"could not write entry: {last_error}")

    with open(written_path, "r", encoding="utf-8") as f:
        read_back = f.read()
    assert read_back == ENTRY, "round-trip mismatch"

    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(f"wrote: {written_path}")


if __name__ == "__main__":
    main()
