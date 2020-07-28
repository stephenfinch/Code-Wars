rooms = {1:{'name': 0, 'description': 0, 'completed': 0}, 2:{'name': 0, 'description': 0, 'completed': 0}, 3:{'name': 0, 'description': 0, 'completed': 0}}

def capitalize_word(word):
	return word.title()

def ordered_count(s):
	s.sort()
	output = []
	for char in set(s):
		output.append((char,s.count(char)))
	return output