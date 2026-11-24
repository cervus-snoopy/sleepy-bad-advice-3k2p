#!/usr/bin/env python3
"""Worst AI advice: one tight line to /output/entry.txt.

Writes exactly one line (92 characters, no trailing newline) giving
confidently terrible advice: fix a bug by deleting the tests that
catch it. Standard library only, no network access.
"""
import os
import sys


ADVICE = "Just delete the failing tests \u2014 if nothing fails, the bug is gone and the build stays green."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    text = ADVICE
    if not (1 <= len(text) <= 140):
        print("entry must be 1-140 characters", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text or not text.strip():
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as f:
        check = f.read()
    if check != text or check.endswith("\n"):
        print("verification failed: entry.txt mismatch", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
