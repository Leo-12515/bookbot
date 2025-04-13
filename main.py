from stats import count_words
from stats import count_char
from stats import sort_dict
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	filepath = sys.argv[1]

	words = count_words(get_book_text(filepath))
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print(f"----------- Word Count ---------- \nFound {words} total words")
	chars = count_char(get_book_text(filepath))
	sorted_list = sort_dict(chars)
	print(f"--------- Character Count -------")
	for char, count in sorted_list:
		print(f"{char}: {count}")
	print("============= END ===============")

main()

