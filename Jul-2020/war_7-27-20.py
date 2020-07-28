rooms = {1:{'name': 0, 'description': 0, 'completed': 0}, 2:{'name': 0, 'description': 0, 'completed': 0}, 3:{'name': 0, 'description': 0, 'completed': 0}}

def capitalize_word(word):
	return word.title()

def ordered_count(s):
	output, seen = [], []
	for char in s:
		if char not in seen:
			output.append((char, s.count(char)))
		seen.append(char)
	return output
