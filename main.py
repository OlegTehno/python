from stats import get_num_words, get_character_frequency, sort_dictionary_by_value
import sys

def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    path = sys.argv[1]
    print(f"Analyzing book found at {path}...")
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    freq = get_character_frequency(book_text)
    sorted_alpha = sort_dictionary_by_value(freq)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_alpha:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()

print(sys.argv)