def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def count_words(text):
	words = text.split()
	count = 0
	for a in words:
		count += 1
	return count

def main():
	words = count_words(get_book_text('books/frankenstein.txt'))
	print(f"{words} words found in the document")
	
main()

