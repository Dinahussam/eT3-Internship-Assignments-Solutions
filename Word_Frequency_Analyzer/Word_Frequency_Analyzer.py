import re
from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt


"""Read a text file and return a Counter of word frequencies."""
def analyze_file(file_path: Path):
    counter = Counter()
    with file_path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            words = re.findall(r"\b[\w']+\b", line.lower())
            counter.update(words)
    return counter


"""Print the top N most common words and their counts."""
def print_top_words(counter: Counter, top_n: int):
    print(f"\nTop {top_n} words:")
    for word, count in counter.most_common(top_n):
        print(f"{word}: {count}")


"""Save a bar chart of the top N words to a PNG file."""
def save_chart(counter: Counter, top_n: int, output_file: str = "word_chart.png"):
    if not plt:
        print("matplotlib not installed, cannot save chart.")
        return
    words, counts = zip(*counter.most_common(top_n))
    plt.bar(words, counts)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"Chart saved as {output_file}")


def main():
    top_n = 10
    file_path = Path(input("Enter text file path: "))
    chart = input("Save chart? (y/n): ").lower() == "y"

    if not file_path.exists():
        print("File not found!")
        return

    counter = analyze_file(file_path)
    print_top_words(counter, top_n)

    if chart:
        save_chart(counter, top_n)


if __name__ == "__main__":
    main()