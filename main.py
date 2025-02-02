def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        count_words(file_contents)
        dict = count_characters(file_contents)
        list_of_characters_dict = [{"name": char, "num": count} for char, count in dict.items()]
        list_of_characters_dict.sort(reverse=True, key=sort_on)
        
        for char_dict in list_of_characters_dict:
            print(f"The '{char_dict['name']}' character was found {char_dict['num']} times")
        print("--- End report ---")
        


def count_words(text):
    count = len(text.split())
    print(f"{count} words found in the document")



def count_characters(text):
    lowered_text = text.lower()
    occurrences = {}
        
    for char in lowered_text:
        if char.isalpha():
            if char not in occurrences:
                occurrences[char] = 1
            else:
                occurrences[char] += 1
    return occurrences


def sort_on(dict):
    return dict["num"]


   


main()



