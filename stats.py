def count_words(text):
        words = text.split()
        count = 0
        for a in words:
                count += 1
        return count

def count_char(characters):
	chars = characters.lower()
	chars_dict = {}
	for i in chars:
		if i in chars_dict:
    			chars_dict[i] = chars_dict[i] + 1
		else:
    			chars_dict[i] = 1
	return chars_dict

def sort_dict(dict):
	sorting = {char: count for char, count in dict.items() if char.isalpha()}
	sorted_chars = sorted(sorting.items(), key=lambda pair: pair[1], reverse=True)
	return sorted_chars
