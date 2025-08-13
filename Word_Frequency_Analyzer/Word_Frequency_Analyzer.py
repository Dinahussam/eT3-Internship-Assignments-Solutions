import re
from collections import Counter
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def analyze_file(file_path: Path):
    """
    Reads a text file and counts the frequency of each word.

    Args:
        file_path (Path): Path to the text file.

    Returns:
        Counter: A Counter object mapping words to their frequency counts.
    """
    counter = Counter()
    with file_path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            words = re.findall(r"\b[\w']+\b", line.lower())
            counter.update(words)
    return counter


def print_top_words(counter: Counter, top_n: int):
    """
    Prints the top N most frequent words from the Counter.

    Args:
        counter (Counter): Word frequency counter.
        top_n (int): Number of top words to display.
    """
    print(f"\nTop {top_n} words:")
    for word, count in counter.most_common(top_n):
        print(f"{word}: {count}")


def save_chart(counter: Counter, top_n: int, output_file: str = "word_chart.png"):
    """
    Saves a bar chart of the top N words to a file.

    Args:
        counter (Counter): Word frequency counter.
        top_n (int): Number of top words to include in the chart.
        output_file (str, optional): Filename for the saved chart. Defaults to "word_chart.png".
    """
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
    """
    Main function to run the word frequency analyzer.

    - Prompts the user for a text file path.
    - Displays the top 10 most frequent words.
    - Optionally saves a bar chart of the word frequencies.
    """
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