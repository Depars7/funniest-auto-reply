"""Write one funny out-of-office auto-reply line to /output/entry.txt.

Standard library only. The file's content is exactly the line's
UTF-8 bytes -- no trailing newline -- so repeated runs are
byte-identical. The bounty gate is 1-159 characters, so the line is
validated before it is written.
"""

import os

LINE = (
    "I'm off today. I left my inbox with my intern, Clippy. "
    "He says your email is 'looking into it.' Forever."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(line):
    """The bounty gate: one line, 1-159 characters, non-blank."""
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    text = line.strip()
    if not text:
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 159:
        raise ValueError("entry must be 1-159 characters")
    if "\n" in line or "\r" in line or "\t" in line:
        raise ValueError("entry must be a single line")
    return text


def write_entry(line):
    """Write the line's exact bytes, no trailing newline.

    Only the file gets a chmod. Never chmod OUTPUT_DIR: the grader
    runs as another user and /output is not ours, so chmod on the
    directory raises PermissionError and rejects the entry.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    expected = line.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(expected)
    # The grader collects outputs as another user than the one the
    # program runs as: leave the file readable by all.
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back check: prove the bytes on disk are exactly the line,
    # so a silent write failure can never pass as a valid entry.
    with open(OUTPUT_PATH, "rb") as fh:
        actual = fh.read()
    if actual != expected:
        raise ValueError("read-back mismatch: entry.txt differs from LINE")


def main():
    line = validate(LINE)
    write_entry(line)


if __name__ == "__main__":
    main()
