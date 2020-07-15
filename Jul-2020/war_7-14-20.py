def get_middle(s):
	s = list(s)
	while len(s) > 2:
		s = s[1:-1]
	return ''.join(s)