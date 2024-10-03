def main(filename):
    with open(filename, "r") as f:
        text = f.read()

    word_count = count_words(text)
    char_count = count_characters(text)
    print(f"--- Begin report of {filename}---")
    print(f"{word_count} words found in the document")
    print()
    for char, count in char_count.items():
        print(f"The ''{char}' character was found {count} times")


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

main(filename="books/frankenstein.txt")