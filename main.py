import sys
from stats import count_words, chars_amounts, dict_to_sorted_dicts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text("./" + book_path)
    words_count = count_words(book_text)
    chars_amounts_dict = chars_amounts(book_text)
    dicts_chars_reversed = dict_to_sorted_dicts(chars_amounts_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for dict in dicts_chars_reversed:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

main()
