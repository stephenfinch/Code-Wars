alphabet = 'qwertyuiopasdfghjklzxcvbnm'
def is_pangram(s):
	for char in alphabet:
		if s.lower().count(char) == 0:
			return False
	return True