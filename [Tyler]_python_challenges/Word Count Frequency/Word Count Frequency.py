def count_words(file_path: str) -> dict[str, int]:
    """
    Reads a text file and returns a dictionary with word counts.

    Args:
        file_path: Path to the .txt file.

    Returns:
        Dictionary where keys are words and values are counts.
    """
    from collections import defaultdict
    import re

    word_count = defaultdict(int)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Use regex to extract words; ignore punctuation and make lowercase
                words = re.findall(r'\b\w+\b', line.lower())
                for word in words:
                    word_count[word] += 1
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")

    return dict(word_count)

