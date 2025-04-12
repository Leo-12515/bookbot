from stats import count_words
from stats import count_char
from stats import sort_dict

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents


def main():
	words = count_words(get_book_text('books/frankenstein.txt'))
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print(f"----------- Word Count ---------- \nFound {words} total words")
	chars = count_char(get_book_text('books/frankenstein.txt'))
	sorted_list = sort_dict(chars)
	print(f"--------- Character Count -------")
	for char, count in sorted_list:
		print(f"{char}: {count}")
	print("============= END ===============")

main()

