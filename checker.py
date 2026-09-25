import hashlib
from pathlib import Path

folder = Path (__file__).parent
file_path = folder / "sample.txt"

file_data = file_path.read_bytes()
current_hash = hashlib.sha256(file_data).hexdigest()
print("File fingerprint:", current_hash)

baseline_path = folder / "baseline.txt"
if not baseline_path.exists():
    baseline_path.write_text(current_hash)
    print("Baseline saved. Run again to check for changes.")
else:
    saved_hash = baseline_path.read_text().strip()
    if current_hash == saved_hash:
        print("UNCHANGED")
    else:
        print("MODIFIED")
        