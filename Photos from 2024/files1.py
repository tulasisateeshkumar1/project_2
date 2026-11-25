from pathlib import Path
import shutil

source_dir = Path("E:phone backup/tulasisatishkumar/takeout-20261024T065328Z-1-002")
dest_dir = Path("E:phone backup/tulasisatishkumar/takeout-20261024T065328Z-1-002_1")
dest_dir.mkdir(parents=True, exist_ok=True)

for jpg_path in source_dir.rglob("*"):
    if jpg_path.is_file() and jpg_path.suffix.lower() in {".jpg", ".jpeg"}:
        target = dest_dir / jpg_path.name
        # Avoid overwriting files with the same name
        if target.exists():
            target = dest_dir / f"{jpg_path.parent.name}_{jpg_path.name}"
        shutil.copy2(jpg_path, target)
