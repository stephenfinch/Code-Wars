def solve(s):
	v, count, totals = 'aeiou', 0, []
	for char in s:
		if char in v:
			count += 1
		else:
			totals.append(count)
			count = 0
	return max(totals)