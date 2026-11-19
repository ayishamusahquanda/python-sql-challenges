import re
from collections import Counter

def most_common_word(sentence):
    if not isinstance(sentence, str):
        raise TypeError("Sentence must be a string.")
    if sentence.strip() == "":
        return None

    cleaned = re.sub(r'[^\w\s]', '', sentence.lower())

    words = cleaned.split()

    if not words:
        return None

    counts = Counter(words)

    max_counts = max(counts.values())
    for word in words:
        if counts[word] == max_counts:
            return word


tests = [
    "What and what am I doing today?",
    "The cat, the dog, the cat, and the mouse are friends.",
    "apple, banana, grapes",
    "",
    "!!! ???"
]
for t in tests:
    print(repr(t), "->", most_common_word(t))
