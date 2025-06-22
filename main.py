
from stats import char_count
from stats import word_count
from stats import sort_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    count = word_count(text)
    characters = char_count(text)
    sorted_list = sort_list(characters)
    print_report(book, count, sorted_list)

def get_book_text(book):
    with open(book) as f:
        book = f.read()
    return book


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
