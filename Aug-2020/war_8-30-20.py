set_ = 'abcdefghijklmnopqrstuvwxyz'

def missing_alphabets(s):
	s.sort()
	output, repeat = [], 0
	for char in set_:
		if char not in s: