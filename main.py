from stats import count_words

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents


def main():
	words = count_words(get_book_text('books/frankenstein.txt'))
	print(f"{words} words found in the document")

main()

