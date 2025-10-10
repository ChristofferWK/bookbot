from stats import character_count
from stats import sort_dictionary
from stats import sort_list_of_dicts
from stats import word_count
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
frankenstein_count = character_count(get_book_text(book_path))
def main():
    unsorted_list = sort_dictionary(frankenstein_count)
    sorted_list = sort_list_of_dicts(unsorted_list)
    words = word_count(get_book_text(book_path))
    print(f"============ BOOKBOT ============ \nAnalyzing book found at {book_path}... \n----------- Word Count ---------- \nFound {words} total words \n--------- Character Count -------")
    for dictionary in sorted_list:
        if dictionary["char"].isalpha() == True:
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")


main()

