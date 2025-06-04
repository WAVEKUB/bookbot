import sys
from stats import get_num_words, count_characters, sort_count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_book = sys.argv[1]
    contents = get_book_text(path_book)
    num_words = get_num_words(contents)
    count_dict = count_characters(contents)
    sort_count = sort_count_characters(count_dict)
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for char in sort_count:
        key = char["char"]
        value = char["num"]
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")
    
main()
