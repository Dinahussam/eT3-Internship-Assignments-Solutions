import shutil
from pathlib import Path
from collections import defaultdict

# Mapping of file categories to their associated extensions
EXT_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv"],
    "Audio": [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2"],
    "Code": [".py", ".js", ".java", ".c", ".cpp", ".cs", ".html", ".css", ".ts", ".go", ".rs"]
}


def categorize(path: Path):
    """
    Determine the category of a file based on its extension.

    Args:
        path (Path): Path to the file.

    Returns:
        str: The category name (e.g., "Images", "Documents", "Others").
    """
    ext = path.suffix.lower()
    for cat, exts in EXT_MAP.items():
        if ext in exts:
            return cat
    return "Others"


def organize_files(folder: Path, simulate: bool = False):
    """
    Organize files in the given folder into categorized subfolders.

    Args:
        folder (Path): Path to the target folder.
        simulate (bool): If True, display planned moves without actually moving files.
    """
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


def ensure_unique_name(dest: Path):
    """
    Ensure that a file's destination path is unique by appending (1), (2), etc.

    Args:
        dest (Path): Original destination path.

    Returns:
        Path: A unique destination path.
    """
    i = 1
    new_dest = dest
    while new_dest.exists():
        new_dest = dest.parent / f"{dest.stem} ({i}){dest.suffix}"
        i += 1
    return new_dest


def main():
    """
    Main entry point for the script.
    Prompts the user for a folder path and whether to simulate file organization.
    """
    folder_path = Path(input("Enter folder path: "))
    simulate = input("Simulate only? (y/n): ").lower() == "y"
    organize_files(folder_path, simulate)


if __name__ == "__main__":
    main()