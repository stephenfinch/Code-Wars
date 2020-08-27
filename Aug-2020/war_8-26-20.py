def is_isogram(s):
	print(set(s))
	return len(set(s)) == len(s)


print(is_isogram('fasADfes'))