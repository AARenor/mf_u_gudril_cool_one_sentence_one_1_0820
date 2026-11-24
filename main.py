import os
import sys

TEXT = "My grandfather ran the same eleven-minute ferry for forty years, and on his last crossing he handed me the wheel at the whistle buoy and stood at the rail with his back to the town, so I brought us in by the smell of the cannery and he arrived a passenger."

assert 1 <= len(TEXT) <= 280

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as entry:
    entry.write(TEXT)

print(len(TEXT), file=sys.stderr)
