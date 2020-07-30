def solve(s):
	up = 0
	for char in s:
		if char.isupper():
			up += 1
	return s.lower() if up <= len(s)/2 else s.upper()