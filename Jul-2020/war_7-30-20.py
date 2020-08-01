def solve(s):
	up = 0
	for char in s:
		up += 1 if char.isupper()
	return s.lower() if up <= len(s)/2 else s.upper()