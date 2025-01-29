def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))
        print(count_characters(file_contents))


def count_words(text):
    return len(text.split())



def count_characters(text):
    lowered_text = text.lower()
    occurrences = {}
        
    for char in lowered_text:
        if char not in occurrences:
            occurrences[char] = 1
        else:
            occurrences[char] += 1
    return occurrences


main()
