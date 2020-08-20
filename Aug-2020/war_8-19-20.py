def duplicate_encode(word):
	word = list(word.lower())
	output = []
	for char in word:
		if word.count(char) > 1:
			output.append(')')
		else:
			output.append('(')
	return ''.join(output)



print(duplicate_encode("Success"),")())())")