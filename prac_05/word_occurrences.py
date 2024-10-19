"""
CP1404 Practical
Word Occurrences
Estimate: 30 minutes
Actual:   51 minutes
"""

word_count = {}
words_in_string = input("Enter a string: ")
words = words_in_string.split()
for word in words:
    occurrence = word_count.get(word, 0)
    word_count[word] = occurrence + 1
words = list(word_count.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_count[word]}")
