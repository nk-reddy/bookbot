from stats import get_word_count, get_char_count, get_sorted_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read();
        return file_contents;

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file = get_book_text(filepath) 
    char_dict = get_char_count(file)
    sorted_dict = get_sorted_dictionary(char_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f"Found {get_word_count(file)} total words")

    print("--------- Character Count -------")
    for entry in sorted_dict:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()
