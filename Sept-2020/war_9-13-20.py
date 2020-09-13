def reverse_words(text):
	text, output = text.split(' '), []
	for word in text:
		output.append(''.join(reversed(list(word))))
	return ' '.join(output)

print(reverse_words('abc aaaff'))