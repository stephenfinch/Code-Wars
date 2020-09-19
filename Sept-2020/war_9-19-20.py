def solve(s):
	for char in s:
		if char in 'qwertyuiopasdfghjklzxcvbnm':
			s.replace(char, ' ')
	return s