import shutil
from pathlib import Path

source_dir = Path("E:/phone backup/Photos from 2026")
dest_dir = Path("E:/phone backup/Photos from 2026_1")

dest_dir.mkdir(parents=True, exist_ok=True)

# Copies only .jpg files
for jpg in source_dir.glob("*.jpg"):
    jpg.rename(dest_dir / jpg.name)


