def solve(s):
	spaces = []
	for i in range(len(s)):
		if s[i] == ' ':
			spaces.append(i)
	s = s.replace(' ', '')
	s = list(s)
	s.reverse()
	for a in spaces:
		print(a)
		s.insert(' ', a)
	return ''.join(s)


print(solve("i love codewars"),"s rawe docevoli")