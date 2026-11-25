"""One line, no deadline met — make.fun entry program.

Writes the one-line excuse to /output/entry.txt.
"""
# Design notes — why this line should win:
# Fresh angle: the deadline never moved at all — the file just kept being
# renamed final_v2 until the calendar itself gave up. It sounds like
# something a real person would actually say, it is one line with no
# setup, and the blame lands on the calendar, not the worker.

ENTRY = "The deadline never moved. I just renamed the file final_v2 so many times the calendar gave up on me too."

MAX_CHARS = 200
MAX_WORDS = None

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    if MAX_WORDS is not None:
        assert len(ENTRY.split()) <= MAX_WORDS, f"entry is {len(ENTRY.split())} words, limit {MAX_WORDS}"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
