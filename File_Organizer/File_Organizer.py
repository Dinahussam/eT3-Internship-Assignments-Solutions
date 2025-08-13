import shutil
from pathlib import Path
from collections import defaultdict

# File type mapping
EXT_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv"],
    "Audio": [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2"],
    "Code": [".py", ".js", ".java", ".c", ".cpp", ".cs", ".html", ".css", ".ts", ".go", ".rs"]
}


"""Return the category for a given file based on its extension."""
def categorize(path: Path):
    ext = path.suffix.lower()
    for cat, exts in EXT_MAP.items():
        if ext in exts:
            return cat
    return "Others"


"""Organize files in the given folder into categorized subfolders."""
def organize_files(folder: Path, simulate: bool = False):
    if not folder.exists() or not folder.is_dir():
        print("Invalid folder!")
        return

    summary = defaultdict(int)

    for item in folder.iterdir():
        if item.is_file():
            cat = categorize(item)
            dest_dir = folder / cat
            dest_dir.mkdir(exist_ok=True)
            dest = dest_dir / item.name

            if simulate:
                print(f"[SIMULATE] {item.name} -> {dest}")
            else:
                dest = ensure_unique_name(dest)
                shutil.move(str(item), str(dest))
                print(f"Moved {item.name} -> {dest}")
                summary[cat] += 1

    if not simulate:
        print("\nSummary:")
        for cat, count in summary.items():
            print(f"{cat}: {count}")


"""Ensure the destination filename is unique by adding (1), (2), etc."""
def ensure_unique_name(dest: Path):
    i = 1
    new_dest = dest
    while new_dest.exists():
        new_dest = dest.parent / f"{dest.stem} ({i}){dest.suffix}"
        i += 1
    return new_dest


def main():
    folder_path = Path(input("Enter folder path: "))
    simulate = input("Simulate only? (y/n): ").lower() == "y"
    organize_files(folder_path, simulate)


if __name__ == "__main__":
    main()