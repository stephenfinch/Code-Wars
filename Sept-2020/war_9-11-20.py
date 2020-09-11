def is_pangram(s):
	for char in 'qwertyuiopasdfghjklzxcvbnm':
		if char not in s.lower():
			return False
	return True