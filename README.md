# Internship Technical Challenge 2025 – All Tasks Solution

## Overview
This repository contains my solutions for all three options from the **ET3 Internship Technical Assignment**.  
Each task is implemented as a separate Python script with clear structure, docstrings, and optional bonus features.

---

## 1️⃣ File Organizer (Option 1)

### Description
A script that organizes files in a given folder into categorized subfolders such as `Images`, `Documents`, `Videos`, etc., based on file extensions.

### How to Run
```bash
cd File_Organizer
python File_Organizer.py
```
You will be prompted to:
- Enter a folder path.
- Choose whether to **simulate** the moves or actually perform them.

### Features
- Categorizes files by extension.
- **Bonus:** Shows a summary of the number of files moved per category.
- **Bonus:** `simulate` mode to preview actions without moving files.
- Handles duplicate file names by renaming.

---

## 2️⃣ Command-Line To-Do App (Option 2)

### Description
A simple task manager that runs in the terminal, stores tasks in a JSON file, and supports adding, listing, marking as done, and deleting tasks.

### How to Run
```bash
cd Command-Line_To-Do_App
python Command-Line_To-Do_App.py
```
Then use the following commands:
- `add` → Add a new task.
- `list` → Display all tasks.
- `done` → Mark a task as completed.
- `delete` → Delete a task (IDs are reindexed).
- `exit` → Quit the program.

### Features
- Tasks stored in `tasks.json`.
- **Bonus:** Stores creation timestamps in Africa/Cairo local time.
- **Bonus:** Supports priorities and tags.
- Automatically reindexes task IDs after deletion.

---

## 3️⃣ Word Frequency Analyzer (Option 3)

### Description
Reads a `.txt` file, counts the frequency of words, and displays the top 10 most frequent words.

### How to Run
```bash
cd Word_Frequency_Analyzer
python Word_Frequency_Analyzer.py
```
You will be prompted to:
- Enter the path to a `.txt` file.
- Choose whether to save a bar chart of word frequencies.

### Features
- Case-insensitive counting.
- Ignores punctuation.
- **Bonus:** Generates a bar chart of the top words (requires `matplotlib`).
- Handles large files efficiently by streaming line by line.

---

## Language & Tools Used
- **Language:** Python 3.10+
- **Libraries:**
  - `pathlib`, `shutil`, `collections`, `json`, `datetime`, `zoneinfo`, `tzdata`, `re` – standard library
  - `matplotlib` – for charts (optional)

---

## Extra Notes
- All scripts include docstrings and are structured in reusable functions.
- Bonus features from each option are implemented.
- Each file is ready to run directly in the terminal.
