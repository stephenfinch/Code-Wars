def string_letter_count(s):
	s, letters, output = s.lower(), {}, ''
	for char in sorted(s):
		if char in 'qwertyuioplkjhgfdsazxcvbnm':
			letters.update({char: str(s.count(char))})
	for key, value in letters.items():
		output += value+key
	return output