import sys
from stats import count_words, count_each_character, sort_char_count

def get_book_text(book_file):
    with open(book_file) as f:
        book_text = f.read()
    return book_text

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1]
    print(f"Analyzing book found at {book_file}")
    book_text = get_book_text(book_file)
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    char_count = count_each_character(book_text)
    sorted_char_count = sort_char_count(char_count)
    for item in sorted_char_count:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")

main()
